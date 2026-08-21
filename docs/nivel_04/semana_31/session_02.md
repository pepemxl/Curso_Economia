# Semana 31 · Sesión 2: Profundización

## 2. La Santísima Trinidad del Riesgo (Marco de Basilea) (continuación)

### B. Riesgo de Crédito (Credit Risk)
Es el riesgo de que una contraparte (un prestatario o un socio) no cumpla con sus obligaciones de pago (Default) o que su calidad crediticia se deteriore.
* **Componentes Matemáticos:**
  1. **PD (Probability of Default):** Probabilidad de que el cliente quiebre. (Ej. 2%).
  2. **LGD (Loss Given Default):** Si el cliente quiebra, ¿qué porcentaje del préstamo pierdo definitivamente? (Si el préstamo era $100, pero recuperé $40 vendiendo los activos colaterales, mi LGD es 60%).
  3. **EAD (Exposure at Default):** Cuánto dinero le debía el banco al cliente en el exacto momento del default.
* **Medición:** La **Pérdida Esperada (EL - Expected Loss)**, que se calcula multiplicando los tres factores: $EL = PD \times LGD \times EAD$. Los bancos deben apartar este monto de sus utilidades como "provisión de cartera".

### C. Riesgo Operativo (Operational Risk)
Es el riesgo de pérdida resultante de procesos internos inadecuados, personas, sistemas fallidos o eventos externos. Es el riesgo más "humano" y el más difícil de predecir con matemáticas puras.
* **Ejemplos:**
  * *Fraude interno:* Un cajero roba dinero de la bóveda.
  * *Error del sistema:* Un bug informático duplica los depósitos de 10,000 clientes (como ocurrió con Citibank por un error tipográfico que envió $900 millones al fondo de Revlon por error).
  * *Ciberataques:* Hackeos que paralizan los servidores del banco (Ransomware).
  * *Riesgo Legal:* Multas regulatorias por lavado de dinero.
* **Medición:** Como no sigue una distribución Normal limpia, se mide construyendo bases de datos históricas internas (registrando cuántas veces ha pasado un error y cuánto costó) y usando Indicadores Clave de Riesgo (KRI), como "número de transacciones que requieron reversión manual al mes".

---
