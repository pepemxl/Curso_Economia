# Semana 29 · Sesión 4: Caso de Estudio y Evaluación

## 7. Análisis de Caso: El Flash Crash de 2010 y los Algoritmos HFT
*Eres un regulador de la SEC (Comisión de Valores de EE. UU.). Es la tarde del 6 de mayo de 2010. De repente, el Dow Jones se desploma 1,000 puntos en 5 minutos (la mayor caída intradía de la historia).*

Empresas como Accenture, valuadas en $40, llegaron a cotizarse momentáneamente a **$0.01** (un centavo).

**La Autopsia Microestructural:**
No fue un ataque terrorista. Fue un fallo en la interacción entre un orden masiva y los algoritmos de **High-Frequency Trading (HFT)**. Un fondo vendió una orden masiva de futuros E-mini S&P de forma excepcionalmente rápida.
Los algoritmos HFT detectaron la presión vendedora y cancelaron sus órdenes de compra (se retiraron del mercado). Al desaparecer los Market Makers, el libro de órdenes quedó vacío (liquidez evaporada).
Cualquier orden de venta a mercado que entró en esos 5 minutos encontró "cero compradores" hasta que el precio bajó a 1 centavo. 
**Lección:** La electronificación de la bolsa dio velocidad, pero también creó el riesgo de que la liquidez artificial desaparezca en milisegundos en momentos de pánico. Como regulador, introduces los "Circuit Breakers" (disyuntores): si una acción baja más del 5% en 5 minutos, la bolsa suspende su cotización automáticamente para evitar que los algoritmos se devoren los unos a los otros.

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

??? success "Solución del Ejercicio C"

    Estado inicial del libro de órdenes:

    | | Cantidad | Precio | | Precio | Cantidad | |
    |---|---|---|---|---|---|---|
    | **BID** | 2,000 | **$50.00** | ← mejor bid | **$50.10** | 1,000 | ← mejor ask (**ASK**) |
    | | 3,000 | $49.95 | | $50.15 | 4,000 | |

    Spread inicial: $50.10 - 50.00 = \mathbf{\$0.10}$

    **1. Orden límite de compra a $50.05**

    **No se ejecuta. Queda en el libro como nuevo mejor bid.**

    Una orden límite de compra establece el precio **máximo** que aceptas pagar. Para
    que se ejecute contra el libro, debe existir un vendedor dispuesto a vender **a
    ese precio o menos**. El mejor ask está en $\$50.10$, por encima de tu límite de
    $\$50.05$, así que **no hay contraparte**.

    Lo que sí ocurre: tu orden es **más agresiva que el bid existente** de $\$50.00$,
    así que salta a la primera posición del lado comprador por **prioridad de
    precio**:

    | | Cantidad | Precio |
    |---|---|---|
    | **BID** | *tu orden* | **$50.05** ← ahora el mejor bid |
    | | 2,000 | $50.00 |
    | | 3,000 | $49.95 |

    El spread se estrecha de $\$0.10$ a $\$0.05$. Acabas de **aportar liquidez** al
    mercado: en muchas bolsas eso te clasifica como *maker* y paga comisiones
    menores —a veces incluso un rebate— frente al *taker* que consume liquidez.

    Tu orden se ejecutará solo si alguien lanza una venta a mercado o baja su ask a
    $\$50.05$. Podría no ejecutarse nunca: ese es el **riesgo de ejecución** que se
    acepta a cambio de controlar el precio.

    **2. Orden a mercado de compra de 3,000 acciones**

    Una orden a mercado **exige ejecución inmediata** y va consumiendo el libro por
    niveles hasta completar la cantidad (*walking the book*):

    | Nivel | Acciones | Precio | Costo |
    |---|---|---|---|
    | 1.º ask | 1,000 | $50.10 | $50,100 |
    | 2.º ask | 2,000 | $50.15 | $100,300 |
    | | **3,000** | | **$150,400** |

    $$\text{Precio promedio} = \frac{150{,}400}{3{,}000} = \mathbf{\$50.1333}$$

    El primer nivel solo tenía 1,000 acciones, así que las 2,000 restantes se toman
    del siguiente nivel, más caro. Tras la operación, el mejor ask pasa a ser
    $\$50.15$ con 2,000 acciones remanentes: **tu propia orden movió el mercado.**

    **3. Slippage implícito**

    El *slippage* es la diferencia entre el precio que veías al pulsar "comprar"
    ($\$50.10$) y el que realmente pagaste:

    $$\text{Costo ideal} = 3{,}000 \times \$50.10 = \$150{,}300$$

    $$\text{Costo real} = \$150{,}400$$

    $$\mathbf{Slippage = \$100}$$

    Equivalentes: $\$0.0333$ por acción, o **6.65 puntos básicos** del valor operado
    ($0.0333/50.10$).

    !!! warning "Por qué el slippage importa más de lo que parece"
        Cien dólares sobre $\$150{,}000$ suena trivial. Deja de serlo cuando se
        multiplica por la actividad real:

        * Un fondo que rota su cartera 50 veces al año pierde
          $50 \times 6.65 = 332$ puntos básicos anuales — **3.3 % de rentabilidad
          evaporada** solo en ejecución, más que la comisión de gestión.
        * En acciones de baja liquidez, con libros mucho más delgados, una orden
          equivalente puede costar 50 o 100 bps.
        * El slippage **crece de forma no lineal con el tamaño**: comprar 30,000
          acciones en este libro habría barrido varios niveles más.

        Por eso las mesas institucionales rara vez usan órdenes a mercado por
        volúmenes grandes. Fraccionan la ejecución con algoritmos **VWAP** o **TWAP**,
        o buscan contraparte en *dark pools* para no revelar su intención. La regla
        práctica: **orden a mercado cuando lo que importa es la certeza de
        ejecución; orden límite cuando lo que importa es el precio.**
