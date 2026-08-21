# Semana 30 · Sesión 3: Aplicación Práctica

## 5. Ejercicio Práctico: El "Put Protector" (Opciones como Seguro)
Posees 100 acciones de "TechCorp" que cotizan a $150. Tienes miedo de que caigan antes de fin de año por la subida de tasas, pero no quieres venderlas hoy (para no pagar impuestos por ganancias).

**La jugada con Opciones:**
Compras un **Put** con un Strike (precio de venta garantizado) de $140, pagando una **Prima de $5 por acción**. Costo total del "seguro": $500 (100 x $5).

**Escenarios al Vencimiento:**
1. **La acción sube a $180:** El Put expira sin valor (pierdes la prima de $500). Pero tus acciones valen $18,000. Ganancia neta: $3,000 - $500 = $2,500. El seguro te costó $500, pero protegiste tu ganancia al alza.
2. **La acción se desploma a $100:** Activas tu Put. Tienes el derecho de vender tus acciones a $140, aunque en el mercado valgan $100.
   * Sin el Put: Perderías $5,000 (de $150 a $100).
   * Con el Put: Pierdes ($150 - $140) + $5 de prima = $15 por acción. Pérdida total $1,500. *El Put limitó tu pérdida matemáticamente, salvándote de la catástrofe.*
