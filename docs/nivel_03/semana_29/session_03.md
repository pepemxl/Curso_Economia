# Semana 29 · Sesión 3: Aplicación Práctica

## 6. Ejercicio Práctico: Leyendo el Libro de Órdenes y el Slippage
Estás operando acciones de "TechFlow". Miras el libro de órdenes de tu plataforma de trading:
* **Compradores (Bid):** 500 acciones a $20.00 | 1,000 acciones a $19.99
* **Vendedores (Ask):** 200 acciones a $20.05 | 2,000 acciones a $20.08

**Escenario A (Orden Límite):** Envías una orden límite para vender 1,000 acciones a $20.00. Tu orden no se ejecuta, sino que pasa a engrosar el lado de los vendedores (Ask) en el libro. No pagas Spread, pero incurres en riesgo de mercado (si el precio baja, no vendiste nada).

**Escenario B (Orden a Mercado):** Necesitas salir apurado. Envías una orden a mercado para **comprar 500 acciones**.
* El sistema cruza tu orden contra el Ask.
* Las primeras 200 acciones se compran a $20.05.
* No hay más volumen a $20.05, por lo que las 300 acciones restantes suben al siguiente nivel: $20.08.
* **Precio Promedio Pagado:** $(200 \times 20.05) + (300 \times 20.08) = 4,010 + 6,024 = \$10,034$.
* *Slippage:* Separaste $10,025 (500 x $20.05) pero gastaste $10,034. El deslizamiento te costó $9 extra. El spread te afectó.
