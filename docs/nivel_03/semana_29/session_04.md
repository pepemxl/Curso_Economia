# Semana 29 · Sesión 4: Caso de Estudio y Evaluación

## 7. Análisis de Caso: El Flash Crash de 2010 y los Algoritmos HFT
*Eres un regulador de la SEC (Comisión de Valores de EE. UU.). Es la tarde del 6 de mayo de 2010. De repente, el Dow Jones se desploma 1,000 puntos en 5 minutos (la mayor caída intradía de la historia).*

Empresas como Accenture, valuadas en $40, llegaron a cotizarse momentáneamente a **$0.01** (un centavo).

**La Autopsia Microestructural:**
No fue un ataque terrorista. Fue un fallo en la interacción entre un orden masiva y los algoritmos de **High-Frequency Trading (HFT)**. Un fondo vendió una orden masiva de futuros E-mini S&P de forma excepcionalmente rápida.
Los algoritmos HFT detectaron la presión vendedora y cancelaron sus órdenes de compra (se retiraron del mercado). Al desaparecer los Market Makers, el libro de órdenes quedó vacío (liquidez evaporada).
Cualquier orden de venta a mercado que entró en esos 5 minutos encontró "cero compradores" hasta que el precio bajó a 1 centavo. 
**Lección:** La电子电ication de la bolsa diovelocidad, pero también creó el riesgo de que la liquidez artificial desaparezca en milisegundos en momentos de pánico. Como regulador, introduces los "Circuit Breakers" (disyuntores): si una acción baja más del 5% en 5 minutos, la bolsa suspende su cotización automáticamente para evitar que los algoritmos se devoren los unos a los otros.

---

## 8. Tareas y Evaluación de la Semana 29

**A. Lectura Obligatoria:**
* *Market Microstructure Theory* (O'Hara, Maureen) - Lecturas introductorias sobre Liquidez y Bid-Ask Spread.
* *Lectura opcional/Documental:* "The Wall Street Code" o leer sobre el modelo de negocio de Robinhood y Citadel Securities.

**B. Preguntas de Reflexión:**
1. Si tuvieras que ejecutar una orden masiva de venta de $1,000,000 en una empresa de baja liquidez (small-cap), explicarías por qué usar una orden a mercado sería un suicidio financiero debido al Slippage. ¿Qué tipo de orden usarías en su lugar?
2. Describe el modelo económico del PFOF (Payment for Order Flow). Desde la perspectiva del Market Maker (ej. Citadel Securities), ¿por qué les resulta rentable pagarle a un broker (ej. Robinhood) por enviarle las órdenes de sus clientes minoristas?

**C. Ejercicio Práctico a entregar:**
Observas el siguiente Libro de Órdenes para las acciones de la empresa "BlueChip Inc":
* **Bid:** 2,000 @ $50.00 | 3,000 @ $49.95
* **Ask:** 1,000 @ $50.10 | 4,000 @ $50.15

Contesta:
1. Tienes una orden límite de **compra a $50.05**. Explica exactamente qué ocurre con tu orden una vez que la envías al mercado. ¿Se ejecuta? ¿Cómo se posiciona en el libro?
2. Tienes una orden a mercado de **compra de 3,000 acciones**. Calcula matemáticamente el precio promedio al que se te ejecutará la orden completa, detallando cuántas acciones compras a $50.10 y cuántas a $50.15.
3. Calcula el Slippage implícito (cuánto dinero extra pagaste por encima del mejor precio de venta Ask disponible en el momento en que presionaste el botón de "comprar").
