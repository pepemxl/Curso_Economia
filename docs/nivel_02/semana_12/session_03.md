# Semana 12 · Sesión 3: Aplicación Práctica

## 6. Ejercicio Práctico: Equivalencia y Fisher

**Parte A: Equivalencia de Tasas**
Eres el CFO de una empresa y debes elegir entre dos préstamos:
* **Banco A:** Ofrece una tasa nominal del **12% capitalizable mensualmente** ($m=12$).
* **Banco B:** Ofrece una tasa nominal del **12.36% capitalizable trimestralmente** ($m=4$).

*¿Son equivalentes estos préstamos? Vamos a calcularlo.*
1. Paso 1: Encontrar la tasa efectiva del periodo para ambos.
   * Banco A: $i_A = 12\% / 12 = 1\%$ mensual.
   * Banco B: $i_B = 12.36\% / 4 = 3.09\%$ trimestral.
2. Paso 2: Llevar ambos a una medida común (ej. Tasa Efectiva Anual o EAR).
   * $EAR_A = (1 + 0.01)^{12} - 1 = 1.1268 - 1 = 12.68\%$
   * $EAR_B = (1 + 0.0309)^4 - 1 = 1.1268 - 1 = 12.68\%$
* **Conclusión:** ¡Son matemáticamente equivalentes! El Banco B pone un número nominal ligeramente más alto para que parezca peor, pero al capitalizar trimestralmente, la Tasa Efectiva es idéntica. Ambos préstamos costarán lo mismo.

**Parte B: Ecuación Exacta de Fisher**
Un fondo de inversión rindió el año pasado una rentabilidad nominal del **24%**. La inflación reportada fue del **12%**.
El gerente del fondo dice: "¡Generamos un 12% de rentabilidad real para nuestros clientes!"
* **Cálculo Exacto:**
  $r = \frac{1 + 0.24}{1 + 0.12} - 1 = \frac{1.24}{1.12} - 1 = 1.1071 - 1 = 0.1071$
* **Conclusión:** El gerente está mintiendo o es un mal matemático. Con la fórmula aproximada da 12%, pero con la fórmula exacta de Fisher, el rendimiento real para el inversor fue del **10.71%**. El 1.29% restante se perdió por el efecto compuesto de la inflación.

---

## Tercer ejercicio: la consistencia entre flujos y tasa

Este es el error más caro de la modelación financiera, y también el más silencioso: nadie te
avisa, simplemente el VAN sale mal.

Un proyecto genera, **a precios de hoy**, un flujo real constante de $\$100$ anuales durante
3 años. La inflación esperada es del **5 %** y la tasa nominal exigida del **12,05 %**.

**Método 1 — Todo en términos reales**

Tasa real por Fisher exacta:

$$r = \frac{1.1205}{1.05} - 1 = 0.0671 = 6.71\%$$

$$VP = \frac{100}{1.0671} + \frac{100}{1.0671^2} + \frac{100}{1.0671^3}$$

$$VP = 93.71 + 87.81 + 82.29 = \mathbf{\$263.81}$$

**Método 2 — Todo en términos nominales**

Los flujos crecen con la inflación:

| Año | Flujo real | Flujo nominal $100(1.05)^t$ | Descuento al 12,05 % | VP |
|---|---|---|---|---|
| 1 | 100 | 105.00 | 0.8925 | 93.71 |
| 2 | 100 | 110.25 | 0.7966 | 87.81 |
| 3 | 100 | 115.76 | 0.7109 | 82.29 |
| | | | **Total** | **263.81** |

**Idéntico resultado.** Ambos métodos son correctos siempre que sean **internamente
consistentes**.

**El error: mezclar.** Si descontaras los flujos **reales** ($100$ cada año) a la tasa
**nominal** ($12{,}05\%$):

$$VP_{erróneo} = \frac{100}{1.1205} + \frac{100}{1.1205^2} + \frac{100}{1.1205^3} = \$239.98$$

**Subestimas el valor en un 9,0 %.** Y a 10 o 20 años el error se vuelve enorme: estarías
rechazando proyectos rentables de forma sistemática.

!!! warning "Dónde se cuela este error en la práctica"
    En un DCF real (Semana 37) el riesgo está en el **valor terminal**. La fórmula de Gordon
    usa un crecimiento perpetuo $g$; si proyectas flujos nominales, $g$ debe incluir la
    inflación esperada (por ejemplo, 2 % real + 2 % inflación = 4 % nominal). Si usas un $g$
    real con flujos nominales, subvaluas la empresa de forma dramática.

    La regla es de una sola línea: **si el flujo lleva inflación, la tasa también; si no la
    lleva, la tasa tampoco.**

---

## Cuarto ejercicio: la inflación y los impuestos

Aquí está el golpe que casi nadie modela. Inviertes $\$10,000$ en un bono que paga **10 %
nominal**. La inflación es del **7 %** y el impuesto sobre rendimientos financieros es del
**30 %**.

**Paso 1 — Rendimiento nominal antes de impuestos**

$$10{,}000 \times 10\% = \$1{,}000$$

**Paso 2 — El fisco cobra sobre el rendimiento NOMINAL, no el real**

$$\text{Impuesto} = 1{,}000 \times 30\% = \$300$$

$$\text{Rendimiento neto} = \$700 \quad \Rightarrow \quad i_{neto} = 7.0\%$$

**Paso 3 — Rendimiento real después de impuestos (Fisher exacta)**

$$r = \frac{1.07}{1.07} - 1 = \mathbf{0.00\%}$$

**Tu poder adquisitivo no creció ni un centavo**, pese a haber cobrado $\$700$ y a que la tasa
del cartel decía 10 %.

**Paso 4 — ¿Y si la inflación sube al 9 %?**

$$r = \frac{1.07}{1.09} - 1 = -1.83\%$$

**Pierdes poder adquisitivo mientras pagas impuestos por una ganancia que no existe.**

!!! danger "El impuesto invisible sobre el capital"
    La combinación de inflación e impuestos nominales genera lo que los economistas llaman
    **arrastre fiscal por inflación** (*inflation tax drag*): el Estado grava una ganancia
    puramente nominal como si fuera real.

    La tasa nominal que necesitas para conservar el poder adquisitivo es:

    $$i_{requerida} = \frac{\pi}{1 - t}$$

    Con 7 % de inflación y 30 % de impuesto: $0.07/0.70 = \mathbf{10\%}$ — exactamente lo que
    pagaba el bono, de ahí el resultado de cero.

    **Implicaciones prácticas:**

    * En entornos inflacionarios, los instrumentos **indexados a la inflación** (TIPS,
      Udibonos, bonos UF) protegen mucho mejor, aunque su tratamiento fiscal también varía.
    * Las **cuentas con diferimiento fiscal** (planes de pensiones) valen mucho más de lo que
      parece, porque el impuesto diferido capitaliza a tu favor.
    * Al comparar inversiones, la métrica correcta no es el rendimiento nominal ni el real:
      es el **rendimiento real después de impuestos**. Es la única que dice qué puedes comprar.

---
