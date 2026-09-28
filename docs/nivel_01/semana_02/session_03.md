# Semana 2 · Sesión 3: Aplicación Práctica

## 5. Ejercicio Práctico: Elasticidad Precio e Ingresos

Eres el gerente de marketing de una empresa de refrescos. El precio actual de tu botella es de $2.00 y vendes 100,000 unidades al mes (Ingreso total = $200,000).
Decides subir el precio a $2.50 (+25%) para mejorar los márgenes. Como resultado, las ventas caen a 80,000 unidades (-20%).

**Cálculo de la Elasticidad:**
* $E_p = \frac{-20\%}{+25\%} = -0.8$ (Valor absoluto: $0.8$)

**Interpretación Financiera:**
La demanda es **inelástica** ($0.8 < 1$). 
* Ingreso antes: $2.00 \times 100,000 = \$200,000$
* Ingreso después: $2.50 \times 80,000 = \$200,000$

*Conclusión:* ¡Aproximadamente los ingresos se mantuvieron iguales! Al ser inelástica, la subida de precio no destruyó las ventas. (Nota: En la realidad, se debe también calcular el costo marginal; si vendes menos unidades, podrías estar ahorrando costos de producción, mejorando el margen de beneficio final).

---

## Segundo ejercicio: cuando la demanda es elástica

La misma empresa de refrescos lanza una **bebida energética premium**. Precio actual $4.00,
ventas de 50,000 unidades al mes. Sube el precio a $4.60 (+15 %) y las ventas caen a 39,500
unidades (−21 %).

$$E_p = \frac{-21\%}{+15\%} = -1.4 \qquad |E_p| = 1.4$$

**La demanda es elástica.** Veamos el destrozo:

| | Antes | Después |
|---|---|---|
| Precio | $4.00 | $4.60 |
| Unidades | 50,000 | 39,500 |
| **Ingreso total** | **$200,000** | **$181,700** |

**Se perdieron $18,300 de ingresos (−9,2 %) por subir el precio.** Con demanda elástica, la
receta correcta para aumentar ingresos es exactamente la contraria: **bajar** el precio.

---

## Tercer ejercicio: el precio que maximiza el beneficio

Los dos casos anteriores miran solo el **ingreso**. Un gerente serio mira el **beneficio**.
Volvamos al refresco original, ahora con costos:

* Costo variable unitario: **$1.20**
* Costos fijos mensuales: **$50,000**

| | Precio $2.00 | Precio $2.50 |
|---|---|---|
| Unidades | 100,000 | 80,000 |
| Ingreso | 200,000 | 200,000 |
| (−) Costo variable | (120,000) | (96,000) |
| **Margen de contribución** | **80,000** | **104,000** |
| (−) Costos fijos | (50,000) | (50,000) |
| **Beneficio operativo** | **30,000** | **54,000** |

**El beneficio subió un 80 %**, aunque el ingreso no se movió ni un dólar.

La razón: vender 20,000 unidades menos ahorró $24,000 de costo variable que caen íntegros al
resultado. El análisis de la sesión anterior, que concluía "los ingresos se mantuvieron
iguales", **subestimaba enormemente el acierto de la decisión**.

Comprobación con el markup de Lerner: con $|E_p| = 0.8$, la fórmula pediría un margen de
$1/0.8 = 125\%$ sobre el costo marginal, es decir un precio óptimo aún más alto. Cuando la
elasticidad es menor que 1, la empresa **no está maximizando**: siempre le conviene subir el
precio hasta entrar en el tramo elástico de la curva.

!!! danger "Errores frecuentes al calcular elasticidades"
    1. **Usar la variación simple en lugar de la del punto medio.** Subir de 2.00 a 2.50 es
       +25 %, pero bajar de 2.50 a 2.00 es −20 %. ¡La misma variación da elasticidades
       distintas según la dirección! La fórmula del arco lo resuelve usando el promedio como
       base:
       $$E_p = \frac{(Q_2-Q_1)/[(Q_1+Q_2)/2]}{(P_2-P_1)/[(P_1+P_2)/2]}$$
       Con nuestros datos: $\frac{-20{,}000/90{,}000}{0.50/2.25} = \frac{-0.2222}{0.2222} = -1.0$.
       ¡La demanda resulta ser **unitaria**, no inelástica! Por eso el ingreso no cambió: es la
       definición exacta de elasticidad unitaria.
    2. **Confundir el signo.** La elasticidad precio es negativa por definición; se interpreta
       en valor absoluto. Pero en la elasticidad **cruzada** el signo es la respuesta: positivo
       = sustitutos, negativo = complementarios. Nunca la pases a valor absoluto.
    3. **Suponer que la elasticidad es constante a lo largo de la curva.** En una demanda lineal
       la elasticidad **cambia en cada punto**: es elástica en la parte alta (precios altos) e
       inelástica en la baja. El ingreso total se maximiza justo en el punto medio, donde
       $|E_p| = 1$.
    4. **Atribuir a la elasticidad efectos que son de otra variable.** Si al subir el precio
       cayeron las ventas *pero además* entró un competidor nuevo, no todo el efecto es del
       precio. Aislar la causa es el trabajo de la regresión múltiple (Semana 16).

---
