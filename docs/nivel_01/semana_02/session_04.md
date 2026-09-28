# Semana 2 · Sesión 4: Caso de Estudio y Evaluación

## 6. Análisis de Caso: El error de la aerolínea
Una aerolínea de bajo costo vuela a destinos turísticos y a destinos de negocios.
*   **Ruta Turística:** Muy elástica. Si el precio sube un 10%, la demanda cae un 25% (la gente simplemente se va a Cancún en lugar de Capri, o se queda en casa).
*   **Ruta de Negocios:** Muy inelástica. Si el precio sube un 10%, la demanda solo cae un 2% (los ejecutivos *tienen* que ir a cerrar el contrato).

La aerolínea, sin analizar elasticidades, sube el precio de todos sus boletos en un 10% pensando que aumentará sus ingresos.
*   **Resultado Ruta de Negocios:** Ingresos suben. (La caída del 2% en volumen se compensa sobradamente con el +10% de precio).
*   **Resultado Ruta Turística:** Ingresos se desploman. (La caída del 25% en volumen destruye cualquier beneficio del +10% de precio).
*   **Lección Financiera:** En la modelación de ingresos en Excel, **no puedes aplicar un mismo incremento de precios (Price Uplift) a toda la cartera de productos**. Debes segmentar por elasticidad.

---


## 7. Tareas y Evaluación de la Semana 2

**A. Lectura Obligatoria:**
* Mankiw, N. Gregory. *Principios de Economía*. Capítulo 5 (La elasticidad y su aplicación).

**B. Preguntas de Reflexión:**
1. ¿Por qué la demanda de mensajería instantánea (WhatsApp) es altamente elástica? ¿Qué pasaría con sus ingresos si de repente cobraran $1 por cada mensaje enviado?
2. Diferencia entre un bien inferior y un bien normal. Da un ejemplo de cómo una recesión económica podría hacer que un bien inferior aumente sus ventas.

**C. Ejercicio Matemático a entregar:**
El mercado de los auriculares inalámbricos tiene las siguientes variaciones:
* El ingreso promedio del consumidor aumenta en un 10%. Como consecuencia, la demanda de auriculares inalámbricos aumenta en un 15%.
* Por otro lado, el precio de los auriculares con cable (un bien relacionado) disminuye en un 8%, lo que provoca que la demanda de los inalámbricos disminuya en un 4%.

Contesta y justifica:
1. Calcula la Elasticidad Ingreso y determina qué tipo de bien son los auriculares inalámbricos según el ingreso.
2. Calcula la Elasticidad Cruzada y explica la relación (sustitutos o complementarios) entre los auriculares con cable y los inalámbricos.

??? success "Solución del Ejercicio C"

    **1. Elasticidad Ingreso ($E_i$)**

    $$E_i = \frac{\%\Delta Q_d}{\%\Delta \text{Ingreso}} = \frac{+15\%}{+10\%} = +1.5$$

    Interpretación en dos niveles:

    * **$E_i > 0$** → son un **bien normal**: cuando el consumidor gana más, compra más.
    * **$E_i > 1$** → además son un **bien de lujo (superior)**: la demanda crece
      *más que proporcionalmente* que el ingreso. Por cada 1 % que sube el ingreso,
      las ventas suben 1.5 %.

    **Lectura financiera:** un bien con $E_i = 1.5$ es **cíclico**. En una
    expansión sus ventas se disparan, pero en una recesión caen más rápido que la
    economía. Al proyectar ingresos para esta empresa hay que ligar el crecimiento
    de ventas al ciclo del PIB, no usar una tasa plana.

    **2. Elasticidad Cruzada ($E_c$)**

    Bien X = auriculares inalámbricos; Bien Y = auriculares con cable.

    $$E_c = \frac{\%\Delta Q_x}{\%\Delta P_y} = \frac{-4\%}{-8\%} = +0.5$$

    **$E_c > 0$ → son bienes sustitutos.** El signo es lo que importa, y aquí sale
    positivo porque *ambas* variaciones son negativas: bajó el precio del cable y
    bajó la demanda del inalámbrico. Es justo el comportamiento de un sustituto —
    cuando uno se abarata, el otro pierde clientes.

    La magnitud ($0.5$, menor que 1) dice que la sustitución es **débil**: los
    consumidores no consideran ambos productos totalmente intercambiables,
    probablemente porque valoran la ausencia de cable como un atributo propio.

---
