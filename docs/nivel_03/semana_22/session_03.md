# Semana 22 · Sesión 3: Aplicación Práctica

## 5. Ejercicio Práctico: El Desglose Dupont y el FCF

**Parte A: Análisis Dupont de "AutoLux" vs "FastCar"**
Ambas empresas tienen un ROE del 15%. Analicemos sus motores:

* **AutoLux (Venta de autos de lujo):** 
  Margen Neto = 10% × Rotación Activos = 0.75 × Multiplicador Capital = 2.0 $\rightarrow$ $10\% \times 0.75 \times 2.0 = 15\%$ ROE.
* **FastCar (Concesionario de autos usados):**
  Margen Neto = 2% × Rotación Activos = 5.0 × Multiplicador Capital = 1.5 $\rightarrow$ $2\% \times 5.0 \times 1.5 = 15\%$ ROE.

*Análisis:* AutoLux gana dinero por sus altos márgenes y apalancamiento moderado. FastCar sobrevive vendiendo rápido y con poca deuda. Si el mercado entra en recesión, FastCar puede bajar precios para rotar inventario; AutoLux tiene un margen más cómodo, pero su deuda (2x) la hace vulnerable a subidas de tasas de interés.

**Parte B: Calcular FCFF desde el EBITDA**
Tienes los datos de la empresa "TechBuild":
* EBITDA: $200
* Depreciación: $50 (Por lo tanto, EBIT = $150)
* Tasa de Impuestos: 20%
* CapEx (Inversión en nuevo equipo): $60
* Aumento en Capital de Trabajo (Inventario y cobros): $20

1. **NOPAT:** $EBIT \times (1 - 0.20) = 150 \times 0.8 = \mathbf{\$120}$. *(Esto es el EBIT después de impuestos).*
2. **+ Depreciación:** $+ 50$ *(Gasto contable que no salió del banco, se suma).*
3. **- CapEx:** $- 60$ *(Dinero real que salió del banco para comprar maquinaria).*
4. **- $\Delta$ Capital de Trabajo:** $- 20$ *(Dinero atrapado en inventario/cuentas por cobrar).*
5. **FCFF Total:** $120 + 50 - 60 - 20 = \mathbf{\$90}$

*Conclusión:* Aunque el EBITDA era de $200 (impresionante), el Flujo de Caja Libre real que la empresa generó para repartir a bancos y accionistas es de $90. ¡El EBITDA engañaba al doble!

---

## Tercer ejercicio: del FCFF al FCFE y por qué no se mezclan

Continuando con TechBuild ($FCFF = \$90$), añadimos su estructura financiera:

* Gasto financiero: **$\$25$**
* Tasa de impuestos: **20 %**
* Nueva deuda emitida en el año: **$\$40$**
* Amortización de deuda: **$\$15$**

**Cálculo del FCFE:**

$$FCFE = FCFF - \text{Intereses}(1-t) + \text{Deuda nueva} - \text{Amortización}$$

$$FCFE = 90 - 25(0.80) + 40 - 15 = 90 - 20 + 40 - 15 = \mathbf{\$95}$$

**El FCFE ($\$95$) es mayor que el FCFF ($\$90$).** ¿Cómo puede ser, si el accionista cobra
después que el acreedor?

Porque TechBuild **se endeudó neto en $\$25$** ($40 - 15$) durante el año. Ese dinero entró a
la caja y está disponible para los accionistas. Es caja prestada, no generada — y ahí está la
advertencia: **un FCFE alto sostenido por deuda nueva no es señal de salud**, sino de que el
balance se está apalancando.

**El detalle del $(1-t)$:** se restan los intereses **después de impuestos** porque son
deducibles. El costo real para la empresa de pagar $\$25$ de intereses es $\$20$; los otros
$\$5$ los absorbe el fisco vía menor impuesto. Es el escudo fiscal, otra vez.

!!! danger "La regla que nunca se puede romper"
    Cada flujo tiene **su** tasa de descuento y **su** resultado:

    | Flujo | Se descuenta al… | Da como resultado… |
    |---|---|---|
    | **FCFF** | **WACC** | Enterprise Value → restar deuda neta para llegar al equity |
    | **FCFE** | **$r_e$** (costo del patrimonio) | Equity Value **directamente** |

    **Mezclarlos produce errores de valuación de dos dígitos.** Descontar FCFE al WACC infla el
    valor (el WACC es menor que $r_e$ porque incluye deuda barata); descontar FCFF a $r_e$ lo
    hunde.

    En la práctica el FCFF es el estándar, por dos razones: es **independiente de la estructura
    de capital** (permite comparar empresas con endeudamientos distintos) y es **más estable**,
    porque no oscila con las emisiones y amortizaciones de deuda de cada año.

    El FCFE se reserva para valorar bancos y aseguradoras, donde la deuda **es** el negocio y
    separarla no tiene sentido.

---

## Cuarto ejercicio: cuándo el EBITDA engaña más

TechBuild tiene un EBITDA de $\$200$ y un FCFF de $\$90$: el EBITDA sobreestima la caja en un
122 %. Pero la brecha depende radicalmente del sector. Compara tres empresas con **el mismo
EBITDA de $\$200$**:

| | **SoftCo** (software) | **TechBuild** (industrial) | **MineraX** (minería) |
|---|---|---|---|
| EBITDA | 200 | 200 | 200 |
| Depreciación | 10 | 50 | 90 |
| EBIT | 190 | 150 | 110 |
| NOPAT (20 %) | 152 | 120 | 88 |
| (+) Depreciación | 10 | 50 | 90 |
| (−) CapEx | (15) | (60) | (150) |
| (−) Δ Capital de trabajo | (5) | (20) | (10) |
| **FCFF** | **142** | **90** | **18** |
| **FCFF / EBITDA** | **71 %** | **45 %** | **9 %** |

**Tres empresas con EBITDA idéntico generan 142, 90 y 18 de caja libre.** Un inversionista que
las valorase con el mismo múltiplo EV/EBITDA estaría cometiendo un error grosero.

**La razón está en la intensidad de capital.** La minera necesita reponer maquinaria pesada
constantemente: su CapEx ($150$) supera con creces su depreciación ($90$), señal de que además
está expandiendo. El software casi no tiene activos físicos que reponer.

!!! tip "El ratio que revela la trampa en cinco segundos"
    $$\frac{CapEx}{\text{Depreciación}}: \quad \text{SoftCo } 1.5 \qquad \text{TechBuild } 1.2 \qquad \text{MineraX } 1.7$$

    Y sobre todo:

    $$\frac{FCFF}{EBITDA}$$

    Cuando este ratio es bajo y **estructuralmente** bajo (no por un año de inversión puntual),
    el EBITDA es una métrica engañosa para esa empresa. Es exactamente la trampa que verás
    formalizada en la Semana 38 al comparar múltiplos entre sectores con distinta intensidad de
    capital: para la minera, **EV/EBIT o EV/FCF** son mucho más informativos que EV/EBITDA.

---
