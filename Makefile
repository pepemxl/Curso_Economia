PY := python3.12
PYTHON_VERSION = 3.12
PHP_VERSION = 8.4
VENV := venv
REPONAME=$(basename $(pwd))
DOCKER=docker
DOCKER_COMPOSE = docker-compose
PHP_SERVICE := php_dev
PYTHON_SERVICE := python_dev

# Nombre del contenedor de pruebas
CONTAINER_NAME=python_dev

TEST_PATH = tests/
REPORTS_DIR = reports

.PHONY: all build up down restart clean shell composer-install composer-update logs
.PHONY: build_docs up_docs down_docs restart_docs clean_docs
.PHONY: docs_build docs_serve docs_deps figures figures_deps plantillas help


# Default target
all: build up

# Construir la imagen con docker-compose
build:
	$(DOCKER_COMPOSE) build

# Levantar el contenedor en segundo plano
up:
	$(DOCKER_COMPOSE) up -d

# Conectar al contenedor con una terminal interactiva
shell:
	docker exec -it $(CONTAINER_NAME) bash

# Parar el contenedor
down:
	$(DOCKER_COMPOSE) down

# Eliminar el contenedor y la imagen
clean:
	$(DOCKER_COMPOSE) down -v --rmi local --remove-orphans
#	$(DOCKER_COMPOSE) down --rmi all --volumes --remove-orphans

# Run Composer install in the PHP container
composer-install:
	$(DOCKER_COMPOSE) exec $(PHP_SERVICE) composer install

# Run Composer update in the PHP container
composer-update:
	$(DOCKER_COMPOSE) exec $(PHP_SERVICE) composer update

# View logs for all services
logs:
	$(DOCKER_COMPOSE) logs -f


############# Docs ############
DOCKERFILE_DIR_DOCS := ./src/containers/docs
IMAGE_NAME_DOCS := eco-docs
CONTAINER_NAME_DOCS := eco-docs
PORT_DOCS := 8085

# Construye la imagen Docker usando el Dockerfile en /src/containers/docs/
build_docs:
	$(DOCKER) build -t $(IMAGE_NAME_DOCS) -f $(DOCKERFILE_DIR_DOCS)/Dockerfile .

# Levanta el contenedor y expone el puerto 8085 (con live-reload y montado de volumen)
run_docs:
#	 $(DOCKER) run --rm -it -p $(PORT_DOCS):$(PORT_DOCS) -v $(PWD):/app $(IMAGE_NAME_DOCS)
	$(DOCKER) run --rm -it \
		--name $(CONTAINER_NAME_DOCS) \
		-p $(PORT_DOCS):$(PORT_DOCS) \
		-v $(PWD)/mkdocs.yml:/app/mkdocs.yml \
		-v $(PWD)/docs:/app/docs \
		$(IMAGE_NAME_DOCS)

# Detiene y elimina el contenedor (si está en segundo plano)
clean_docs:
	$(DOCKER) stop $(CONTAINER_NAME_DOCS) || true
	$(DOCKER) rm $(CONTAINER_NAME_DOCS) || true
	$(DOCKER) rmi $(IMAGE_NAME_DOCS) || true

# Atajo para build + run
up_docs: build_docs run_docs

############# Docs: calidad y build local (sin Docker) ############
DOCS_REQS := ./src/containers/docs/requirements.txt

# Instala las dependencias fijadas de la documentacion
docs_deps:
	$(PY) -m pip install -r $(DOCS_REQS)

# Instala lo necesario para regenerar las figuras
figures_deps:
	$(PY) -m pip install -r ./src/requirements-figures.txt

# Build estricto: cualquier warning (enlace roto, clave invalida) falla el build.
# Es el mismo comando que corre la CI.
docs_build:
	mkdocs build --strict

# Servidor local con live-reload, sin necesidad de Docker
docs_serve:
	mkdocs serve -a 127.0.0.1:$(PORT_DOCS)

# Regenera todas las figuras del curso en docs/images/
# Usa el python del venv, que es donde vive matplotlib
FIG_PY := $(if $(wildcard $(VENV)/bin/python),$(VENV)/bin/python,$(PY))
figures:
	@for f in $$(find src -name "fig_*.py" | sort); do \
		echo "$$f"; $(FIG_PY) $$f || exit 1; \
	done

# Regenera las plantillas .xlsx y verifica que reproducen los ejercicios
plantillas:
	@for f in $$(find src -name "xls_*.py" | sort); do \
		echo "$$f"; $(FIG_PY) $$f || exit 1; \
	done
	@echo "--- verificando formulas ---"
	@$(FIG_PY) src/verificar_plantillas.py

# Lista los targets disponibles
help:
	@grep -hE '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}'


################# LOCAL  ENVIRONMENT ############################

.PHONY: local_env
local_env: $(VENV)
	@echo "Installed project in virtual environment..."
	@echo "Linux: Use \"source venv/bin/activate\""
#	@echo "Linux: Run \"poetry install\""
	@echo ${REPONAME}


.PHONY: clean_local_env
clean_local_env: ${VENV}
	rm -rf dist
	rm -rf ${VENV}
	rm -rf poetry.lock
	find . -type f -name *.pyc -delete
	find . -type d -name __pycache__ -delete


.PHONY: clean_local_env_cache
clean_local_env_cache: ${VENV}
	find . -type f -name *.pyc -delete
	find . -type d -name __pycache__ -delete
