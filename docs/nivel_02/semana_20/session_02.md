# Semana 20 · Sesión 2: Profundización

## 4. Las Funciones Clave en Excel para Monte Carlo
Para hacer Monte Carlo sin necesidad de programar en Python o VBA, usamos dos funciones de Excel combinadas:

1. **=ALEATORIO() o =ALEATORIO.ENTRE():** Genera un número al azar entre 0 y 1. Es el "motor aleatorio" de la simulación (representa la probabilidad acumulada).
2. **=INV.NORM(probabilidad; media; desv_estándar):** Toma un número de probabilidad (entre 0 y 1) y lo traduce a un valor real basado en la Campana de Gauss (Distribución Normal de la Semana 15).

* **La Magia:** `=INV.NORM(ALEATORIO(); 10; 1)`
  Excel generará un número aleatorio (ej. 0.45), lo meterá en la inversa de la distribución normal con media 10 y desviación 1, y te arrojará un precio de venta aleatorio de $9.87. Cada vez que presiones F9 (recalcular), Excel lanzará los "dados" y te dará un nuevo escenario completo.

---

