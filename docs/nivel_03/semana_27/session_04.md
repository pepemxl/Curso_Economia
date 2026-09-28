# Semana 27 · Sesión 4: Caso de Estudio y Evaluación

## 5. Análisis de Caso: El error de AOL y la burbuja Dot-Com
*Eres analista de M&A en 1999, justo en el pico de la burbuja de las puntocom. La empresa AOL (proveedor de internet dial-up) anuncia la compra de Time Warner (el gigante de medios y cable) por un valor histórico de **$165 mil millones**.*

La justificación del CEO de AOL fue: *"Sinergias perfectas. Vamos a llevar el contenido de Time Warner por internet a todos los hogares"*. AOL pagó una prima altísima utilizando sus acciones infladas por la burbuja bursátil.

**La Realidad Financiera (El choque de culturas):**
1. **El fracaso de la integración (Sinergias = 0):** AOL era una empresa ágil de tecnología. Time Warner era un burocrático dinosaurio de medios. Los departamentos no lograron integrarse; las sinergias de "cruzar productos" nunca existieron.
2. **El desplome del valor:** La burbuja estalló en 2001. Las acciones combinadas perdieron el 80% de su valor. AOL se arrastró con deuda y activos intangibles (Goodwill) inflados que tuvieron que ser "desvalorizados" (impairment charge) por miles de millones, destruyendo utilidades contables.
3. **Lección de M&A:** M&A no es solo un ejercicio matemático de Excel. El 70% de las fusiones fracasan porque sobreestiman las sinergias operativas y subestiman el "riesgo de integración cultural". Como analista, tu trabajo en una operación de M&A es aplicar un **descuento a las sinergias proyectadas** ( haircut) porque la realidad nunca es tan perfecta como el PowerPoint del banquero de inversión.

---

## 6. Tareas y Evaluación de la Semana 27

**A. Lectura Obligatoria:**
* *Investment Banking: Valuation, Leveraged Buyouts, and Mergers and Acquisitions* (Joshua Rosenbaum & Joshua Pearl). Capítulos sobre M&A y Valuación de Startups.
* *Lectura recomendada:* El artículo de Bill Gurley (Benchmark Capital) "How to value a startup" o videos en YouTube sobre "Term Sheets de Venture Capital".

**B. Preguntas de Reflexión:**
1. ¿Por qué la Tasa Interna de Retorno (TIR) exigida por un fondo de Venture Capital (ej. 50% anual) es tan diferente al WACC de una empresa madura (ej. 9% anual) al evaluar un proyecto? ¿Qué riesgo matemático están cubriendo?
2. En una operación de M&A, si la empresa compradora paga una "Prima" mayor al valor de las sinergias reales creadas, ¿quién se beneficia y quién sale perjudicado? ¿Por qué se dice entonces que "las fusiones suelen pagarse con el dinero de los accionistas de la empresa compradora"?

**C. Ejercicio Matemático a entregar:**
Eres parte de un fondo VC evaluando invertir en "MediTech", una startup de software médico.
* Inversión Requerida: **$5,000,000**
* Tasa de Retorno Objetivo anual exigido por el fondo: **40%**
* Tiempo esperado hasta la salida (Exit): **4 años**
* Se estima que MediTech será adquirida en el Año 4 por un Valor Terminal de **$80,000,000**.

Contesta:
1. Calcula el Valor Post-Money de la startup hoy, descontando el Valor Terminal a 4 años al 40% anual. (Muestra la fórmula $VP = VF / (1+r)^t$).
2. Calcula el Valor Pre-Money de la startup.
3. ¿Qué porcentaje de participación accionaria (Ownership %) debe exigir tu fondo a cambio de los $5 Millones?

??? success "Solución del Ejercicio C"

    **1. Valor Post-Money**

    Se descuenta el valor de salida a la tasa exigida por el fondo:

    $$VP = \frac{VF}{(1+r)^t} = \frac{80{,}000{,}000}{(1.40)^4}$$

    $$(1.40)^4 = 3.8416$$

    $$VP = \frac{80{,}000{,}000}{3.8416} = \mathbf{\$20{,}824{,}656}$$

    **2. Valor Pre-Money**

    $$\text{Pre-Money} = \text{Post-Money} - \text{Inversión}$$

    $$= 20{,}824{,}656 - 5{,}000{,}000 = \mathbf{\$15{,}824{,}656}$$

    La distinción es la que más confusión genera en una negociación: el **pre-money**
    es lo que vale la empresa *antes* de recibir el cheque —el trabajo de los
    fundadores hasta hoy—, y el **post-money** ya incluye los $\$5$ millones que
    acaban de entrar a la caja. El dinero del fondo no desaparece: se convierte en
    activo de la propia empresa.

    **3. Participación accionaria exigida**

    $$\% \text{Ownership} = \frac{\text{Inversión}}{\text{Post-Money}} = \frac{5{,}000{,}000}{20{,}824{,}656}$$

    $$\mathbf{= 24.01\%}$$

    **Comprobación de la lógica del fondo:** con el 24.01 % de una salida de
    $\$80$ millones, el fondo recibiría
    $0.2401 \times 80{,}000{,}000 = \$19.2$ millones. Sobre $\$5$ millones invertidos
    son **3.84×** en 4 años, que anualizado es exactamente
    $3.84^{1/4} - 1 = 40\%$ ✓ — su tasa objetivo.

    !!! note "Por qué un VC exige 40 % anual"
        Un 40 % anual parece usura frente al 8-12 % de una empresa madura. La razón
        no es codicia sino **aritmética de portafolio**: de cada 10 inversiones de un
        fondo de capital de riesgo, típicamente 5 mueren por completo, 3 devuelven
        más o menos lo invertido, y solo 1 o 2 producen el retorno de todo el fondo.

        Ese 40 % es la tasa que **la inversión que sobrevive** debe rendir para
        cubrir a las que no. También compensa la **iliquidez** (el capital queda
        atrapado 4-7 años sin mercado secundario) y la enorme incertidumbre de la
        proyección de salida.

    !!! warning "Lo que este cálculo todavía ignora: la dilución"
        El resultado supone que **no habrá más rondas de financiamiento**, algo casi
        nunca cierto. Si MediTech levanta una Serie B y una Serie C antes de la
        salida, la participación del 24.01 % se **diluye** con cada emisión de
        acciones nuevas.

        Por eso los fondos calculan el porcentaje sobre la **capitalización
        totalmente diluida** (incluyendo el *pool* de opciones para empleados, las
        notas convertibles y los SAFE pendientes), y negocian *cláusulas
        antidilución* y derechos *pro-rata* para mantener su posición. Pedir 24 %
        hoy sin protección puede convertirse en 12 % el día de la salida — y la mitad
        del retorno objetivo.
