# Semana 9 · Sesión 2: Profundización

## 4. El Estado de Cambios en el Patrimonio
Muestra los movimientos en todas las cuentas del Patrimonio (Capital Social, Utilidades Retenidas, Acciones en Tesorería, Reservas) durante el año. 
Su función fundamental es explicar cómo pasó el patrimonio de "X" valor el 1 de enero a "Y" valor el 31 de diciembre.

| Concepto | Explicación |
| :--- | :--- |
| **Utilidad Neta del Año** | Suma al patrimonio (generada por el negocio). |
| **(-) Dividendos Pagados** | Resta al patrimonio (dinero que salió hacia los accionistas). |
| **Emisión de Nuevas Acciones** | Suma al patrimonio (a cambio de dar efectivo a la empresa). |
| **Recompra de Acciones (Treasury Stock)** | Resta al patrimonio (uso de efectivo para reducir acciones en circulación). |

> **💥 Impacto Financiero:** Un analista financiero revisa este estado para ver si la empresa está **diluyendo** al accionista. Si la empresa cada año emite nuevas acciones (increasing share count) para pagar sus deudas, tu porción de la tarta de la empresa se hace más pequeña cada vez, aunque la empresa crezca. Es una señal de alerta roja.

---

## Método directo frente a indirecto

El Flujo de Operación puede presentarse de dos formas que **siempre dan el mismo resultado**:

| | **Método directo** | **Método indirecto** |
|---|---|---|
| Punto de partida | Cobros y pagos reales | Utilidad neta |
| Cómo se construye | Cobros a clientes − pagos a proveedores − pagos de nómina… | Utilidad + partidas no monetarias ± capital de trabajo |
| Claridad | Mucho mayor | Menor, pero informativa |
| Uso real | Raro (< 5 % de las empresas) | **El estándar de facto** |

Las normas contables **prefieren** el método directo por ser más transparente, y sin embargo casi
nadie lo usa. La razón es doble: exige un sistema contable que rastree cada cobro y pago por
categoría, y —más importante— el método indirecto **muestra la reconciliación** entre utilidad y
caja, que es justo lo que un analista quiere ver.

---

## La lectura diagnóstica: el patrón de los tres flujos

El signo combinado de CFO, CFI y CFF dibuja el retrato de una empresa mejor que cualquier ratio
aislado:

| CFO | CFI | CFF | Diagnóstico |
|:---:|:---:|:---:|---|
| **+** | **−** | **−** | **Madura y sana.** Genera caja, invierte y aún devuelve dinero (dividendos, deuda). El perfil ideal. |
| **+** | **−** | **+** | **En expansión.** Genera caja pero necesita financiamiento externo para crecer más rápido. Normal si el crecimiento lo justifica. |
| **+** | **+** | **−** | **En desinversión.** Vende activos para pagar deuda. Puede ser reestructuración sana… o liquidación encubierta. |
| **−** | **−** | **+** | **Startup o problema.** Quema caja y se financia con capital externo. Sostenible solo mientras haya inversores dispuestos. |
| **−** | **+** | **−** | **Alarma máxima.** Pierde caja operando, vende activos y aun así paga deuda. El activo productivo se está desmantelando. |

**La pregunta que hay que hacerse siempre:** ¿la empresa financia sus dividendos con **flujo
operativo** o con **deuda nueva**? Un dividendo pagado con deuda no es un reparto de beneficios:
es una devolución de capital que erosiona el balance, y no es sostenible.

---

## Las trampas de clasificación

Dónde se coloca cada flujo **no es neutral**, porque el CFO es la métrica que más miran los
analistas. Las normas dejan margen, y las empresas lo usan:

* **Intereses pagados.** NIIF permite clasificarlos en operación **o** en financiamiento. US
  GAAP obliga a operación. Una empresa muy endeudada que los lleva a financiamiento presenta un
  CFO artificialmente mejor que un competidor idéntico.
* **Factoring de cuentas por cobrar.** Vender la cartera a un banco convierte lo que sería una
  entrada de operación *futura* en efectivo *hoy*, e infla el CFO del trimestre. Es
  financiamiento disfrazado de operación.
* **Financiamiento a proveedores (*reverse factoring*).** Estirar los pagos a proveedores usando
  un banco intermediario mejora el CFO sin que aparezca deuda en el balance. Fue uno de los
  mecanismos centrales del colapso de Carillion y de Abengoa.
* **Capitalizar en lugar de gastar.** Un desembolso registrado como CapEx sale del CFO y entra
  al CFI. **El efectivo total no cambia, pero el CFO mejora.** Por eso el FCF (que resta el
  CapEx) es a prueba de este truco, y el CFO por sí solo no lo es.

!!! tip "La regla práctica del analista"
    Compara siempre **CFO acumulado de 3-5 años contra utilidad neta acumulada** del mismo
    período. En un negocio sano la relación es cercana a 1 o superior.

    Si durante varios años la utilidad supera sistemáticamente al flujo operativo, la diferencia
    tiene que estar en algún sitio del balance: cuentas por cobrar que no se cobran, inventario
    que no rota o gastos capitalizados. Ninguna de las tres explicaciones es buena.

---
