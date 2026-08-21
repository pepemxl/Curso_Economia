# Semana 25 · Sesión 3: Aplicación Práctica

## 6. Ejercicio Práctico: La Expansión de la Planta
La empresa "AgriCorp" quiere comprar una nueva cosechadora. La máquina cuesta **$10,000** (Inversión Año 0). Generará flujos de caja de **$4,000** al año durante 3 años. El WACC de AgriCorp es del **10%**.

**Cálculo Matemático:**
1. **VAN:**
   * Año 1: $4,000 / (1.10)^1 = $3,636
   * Año 2: $4,000 / (1.10)^2 = $3,305
   * Año 3: $4,000 / (1.10)^3 = $3,005
   * Total VP de Flujos = $9,946
   * VAN = -$10,000 + $9,946 = **-$54**.
   * *Veredicto VAN:* Rechazar. El proyecto está destruyendo $54 de valor presente porque no logra cubrir el WACC.

2. **TIR:**
   * Probamos con multiple tasas. (En Excel: `=TIR(-10000, 4000, 4000, 4000)`).
   * La tasa que hace el VAN cero es **9.70%**.
   * *Veredicto TIR:* Rechazar. La TIR (9.70%) es menor que el WACC (10%). Coincide con el VAN.

3. **Payback Descontado:**
   * Fin del Año 1 recuperamos $3,636 (Falta $6,364).
   * Fin del Año 2 recuperamos $3,305 (Acumulado $6,941. Falta $3,059).
   * En el Año 3 necesitamos $3,059. Ese año generamos $3,005 descontados.
   * No alcanzamos a recuperar la inversión en los 3 años. El proyecto se paga en approx 3.02 años.
   * *Veredicto Payback:* Rechazado. *(Nota: Si el VAN fuera positivo y se recuperara en el año 2.5, el proyecto se aceptaría si la política de la empresa acepta proyectos de hasta 3 años de recuperación).*
