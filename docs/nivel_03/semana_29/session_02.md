# Semana 29 · Sesión 2: Profundización

## 4. Los Intermediarios: ¿Quién es quién en el mercado?
El inversor minorista (tú o yo) no tiene acceso directo al servidor de la bolsa. Necesitamos intermediarios.
1. **Brokers (Agentes):** Ejecutan las órdenes en tu nombre. No compran ni venden para ellos mismos. Cobran una comisión. (Ej. Interactive Brokers, Charles Schwab).
2. **Dealers (Principales):** Compran y venden para su propio inventario. Aceptan el riesgo de mercado. 
3. **Market Makers (Creadores de Mercado):** Son Dealers obligados por la bolsa a mantener liquidez. Si todo el mundo quiere vender y no hay compradores (pánico), el Market Maker está obligado a comprar para que el mercado no se congele. Ganan dinero con el Spread. Aseguran que siempre haya alguien dispuesto a operar.

---

## 5. Comisiones y Costos Ocultos (Microestructura)
El gasto de operar en bolsa no es solo la comisión que te cobra tu broker. Hay costos ocultos que destruyen la rentabilidad de los traders inexpertos:
1. **Costos Explícitos:** Comisión fija por trade (ej. $1 por operación) y el Impuesto a las transacciones financieras (ITF o Tobin Tax en Europa).
2. **El Spread (Costo Implícito):** Si la acción tiene un Bid de $10.00 y un Ask de $10.02. Si compras a mercado y al segundo decides vender, ya perdiste $0.02. El Spread es la ganancia del Market Maker.
3. **Slippage (Deslizamiento):** Ocurre cuando envías una orden de mercado para 10,000 acciones, pero a $10.02 solo hay 500 acciones a la venta. Las siguientes 2,000 se compran a $10.05, y el resto a $10.10. Tu precio promedio de compra se "deslizó" en tu contra por falta de liquidez en el libro.
4. **Impacto en el Mercado (Market Impact):** Si eres un fondo gigante (Ej. BlackRock) y compras $500 millones de una empresa de golpe, tu propia orden de compra empujará el precio al alza. Terminas comprando carísimo.

> **💥 El Escándalo del PFOF (Payment for Order Flow):**
> Brokers como Robinhood ofrecen "Cero Comisiones". ¿Cómo ganan dinero? Vendiendo tus órdenes a Citadel o Virtu (Market Makers gigantes). El Market Maker te ejecuta a $10.01, cuando quizás el precio "real" del mercado era $10.005. El Market Maker te roba una fracción de centavo, y le da un "rebate" a Robinhood. En la práctica, es un costo oculto por la falta de dispersión de precios.
