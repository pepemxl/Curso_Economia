# Semana 11 · Sesión 3: Aplicación Práctica

## 6. Ejercicio Práctico: La tasa efectiva implícita
* **Problema:** Un fondo de inversión exige que dejes $5,000 hoy. Te prometen que en 3 años te devolverán $6,500. No hay pagos intermedios (capitalización anual). ¿Cuál es la rentabilidad anual efectiva de esta inversión?
* **Solución:** Usamos la fórmula de Interés Compuesto para despejar la tasa ($r$).
  $$ VF = VP \times (1 + r)^t $$
  
  $$ 6,500 = 5,000 \times (1 + r)^3 $$
  
  $$ \frac{6,500}{5,000} = (1 + r)^3 $$
  
  $$ 1.30 = (1 + r)^3 $$
  Aplicamos raíz cúbica (potencia de 1/3) a ambos lados:
  $$ (1.30)^{1/3} - 1 = r $$
  
  $$ 1.0913 - 1 = 0.0913 $$
* **Respuesta:** La inversión rinde una **Tasa Efectiva Anual del 9.13% compuesto**.

---

## Segundo ejercicio: la regla del 72 y el poder del tiempo

Antes de calcular nada, conviene tener una intuición. La **regla del 72** aproxima cuántos años
tarda un capital en duplicarse:

$$\text{Años para duplicar} \approx \frac{72}{\text{tasa en \%}}$$

| Tasa anual | Regla del 72 | Cálculo exacto $\ln 2/\ln(1+r)$ |
|---|---|---|
| 3 % | 24.0 años | 23.4 |
| 6 % | 12.0 años | 11.9 |
| 9 % | 8.0 años | 8.0 |
| 12 % | 6.0 años | 6.1 |

Es una aproximación excelente entre el 4 % y el 15 %, y permite hacer sanidad mental sin
calculadora: *"al 9 % el dinero se duplica cada 8 años; en 24 años se multiplica por 8"*.

**Ejercicio.** Dos hermanos ahorran para su jubilación a los 65 años, ambos al **8 % anual**:

* **Ana** invierte $\$2,000$ al año desde los **25 hasta los 35** (10 años, $\$20,000$ en
  total) y **luego no aporta nada más**.
* **Bruno** empieza a los **35** y aporta $\$2,000$ al año hasta los **65** (30 años,
  $\$60,000$ en total).

¿Quién termina con más?

**Ana.** Sus aportes crecen así: el valor de su anualidad a los 35 años es

$$VF_{35} = 2{,}000 \times \frac{(1.08)^{10} - 1}{0.08} = 2{,}000 \times 14.4866 = \$28{,}973$$

y luego crece sola 30 años más:

$$VF_{65} = 28{,}973 \times (1.08)^{30} = 28{,}973 \times 10.0627 = \mathbf{\$291{,}547}$$

**Bruno** acumula durante 30 años:

$$VF_{65} = 2{,}000 \times \frac{(1.08)^{30} - 1}{0.08} = 2{,}000 \times 113.28 = \mathbf{\$226{,}566}$$

| | Ana | Bruno |
|---|---|---|
| Aportado | $20,000 | $60,000 |
| **Valor a los 65** | **$291,547** | **$226,566** |

**Ana aportó un tercio y terminó con un 28,7 % más.** No es una curiosidad aritmética: es la
razón por la que el tiempo es el factor más importante de cualquier plan de inversión, y por
qué el interés compuesto se llama "la octava maravilla".

---

## Tercer ejercicio: la trampa de la tasa promedio

Un fondo publicita: *"rentabilidad promedio del 25 % anual en los últimos dos años"*. Los
retornos fueron **+100 %** el primer año y **−50 %** el segundo.

$$\text{Media aritmética} = \frac{100\% + (-50\%)}{2} = +25\%$$

**Pero si invertiste $\$1,000:**

$$1{,}000 \times 2.00 \times 0.50 = \$1{,}000$$

**No ganaste nada.** Tu rentabilidad real fue del **0 %**.

La medida correcta es la **media geométrica** (o tasa anual compuesta, CAGR):

$$CAGR = \left(\prod (1+r_i)\right)^{1/n} - 1 = (2.00 \times 0.50)^{1/2} - 1 = 1 - 1 = \mathbf{0\%}$$

!!! danger "Aritmética frente a geométrica: cuándo usar cada una"
    * La **media geométrica** responde: *"¿qué rentabilidad constante me habría dado el mismo
      resultado final?"*. Es la única válida para reportar rendimientos históricos.
    * La **media aritmética** responde: *"¿cuál es mi mejor estimación del retorno del próximo
      período?"*. Se usa como insumo esperado en modelos.

    **La geométrica es siempre menor o igual que la aritmética**, y la brecha crece con la
    volatilidad:

    $$\text{Geométrica} \approx \text{Aritmética} - \frac{\sigma^2}{2}$$

    Con volatilidad del 20 %, la diferencia es de 2 puntos porcentuales al año. Por eso la
    industria de fondos tiene tanta tendencia a reportar la aritmética, y por qué la regulación
    obliga cada vez más a publicar la geométrica.

    El otro lado del mismo fenómeno: **perder un 50 % exige ganar un 100 % para volver al punto
    de partida.** Las pérdidas y las ganancias no son simétricas, y esa asimetría es el
    argumento central de la gestión de riesgos (Semana 32).

---
