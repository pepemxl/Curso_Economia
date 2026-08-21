# Semana 29 · Sesión 1: Fundamentos

## 1. Objetivos de la Semana
* Comprender la evolución y arquitectura de una Bolsa de Valores moderna (Parqué físico vs. Redes Electrónicas).
* Entender el "Libro de Órdenes" (Order Book) y la mecánica de formación de precios (Bid-Ask Spread).
* Diferenciar los tipos de intermediarios: Brokers, Dealers y Market Makers.
* Conocer los costos explícitos (comisiones) e implícitos (spread y slippage) y el modelo PFOF (Payment for Order Flow).

---

## 2. La Arquitectura de la Bolsa Moderna
Una bolsa de valores (ej. NYSE, NASDAQ, BME, BIVA) es el mercado secundario por excelencia. Su función es emparejar (match) a compradores y vendedores de forma transparente, segura e instantánea.
* **El Parqué (Pit):** Antiguamente, los brokers gritaban y usaban gestos manuales para negociar. Era ineficiente y lento.
* **El Libro Electrónico (Order Book):** Hoy todo es digital. La bolsa es un servidor informático que recibe millones de órdenes de compra y venta por segundo y las cruza según precio y tiempo. *(El "Parqué" hoy son servidores refrigerados con nitrógeno líquido en Nueva Jersey).*

---

## 3. Formación de Precios: El Libro de Órdenes
El precio de una acción no lo dicta la empresa, ni el gobierno, ni el CEO. Lo dicta la fuerza bruta de la oferta y la demanda en tiempo real (microeconomía pura, Semana 1).

El "Libro" tiene dos lados:
1. **Bid (Demanda / Compradores):** El precio máximo que alguien está dispuesto a pagar por la acción.
2. **Ask u Offer (Oferta / Vendedores):** El precio mínimo al que alguien está dispuesto a vender la acción.
* **El Spread:** Es la diferencia matemática entre el Bid y el Ask. Es el costo oculto de operar.

**Tipos de Órdenes:**
* **Orden a Mercado (Market Order):** "Cómprame esto ya, al precio que sea". Se ejecuta instantáneamente contra el Ask. Garantiza la ejecución, pero no el precio.
* **Orden Límite (Limit Order):** "Cómprame esto, pero máximo a $100". Se inserta en el libro y espera a que el mercado baje. Garantiza el precio, pero no la ejecución.
