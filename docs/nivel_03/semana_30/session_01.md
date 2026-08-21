# Semana 30 · Sesión 1: Fundamentos

## 1. Objetivos de la Semana
* Comprender la utilidad de los derivados como herramientas de cobertura y apalancamiento.
* Diferenciar entre Forwards (OTC) y Futuros (Bolsa organizada).
* Dominar la mecánica de las Opciones (Calls y Puts) y el concepto de "Prima" (Premium).
* Entender cómo funcionan los Swaps y su aplicación en la gestión de deuda corporativa.

---

## 2. Forwards y Futuros: El Compromiso de Comprar/Vender
Ambos son contratos donde dos partes acuerdan comprar/vender un activo en una fecha futura a un precio fijado **hoy**. Eliminan la incertidumbre del precio.

**A. Contratos Forward (OTC - Over The Counter):**
* Son privados, personalizados y se firman directamente entre dos empresas (o entre una empresa y un banco).
* *Ejemplo:* Una panadería acuerda con un agricultor comprar 1,000 toneladas de trigo a $200 la tonelada dentro de 6 meses.
* *Riesgo:* **Contraparte**. Si en 6 meses el trigo vale $500, el agricultor pierde mucho y podría negarse a entregarlo o quebrar. Nadie garantiza el contrato.

**B. Contratos de Futuros (Mercado Organizado):**
* Son estándar y se negocian en una Bolsa (ej. Chicago Mercantile Exchange - CME).
* **La Cámara de Compensación (Clearinghouse):** La bolsa actúa como intermediario. Tú no compras al agricultor, le compras a la bolsa. La bolsa *garantiza* el contrato.
* **Margen (Margin):** Para evitar que la gente quiebre y no pague, la bolsa exige un depósito de garantía (Margen). Si el precio se mueve en tu contra, te hacen un "Llamado de Margen" (Margin Call) pidiéndote más efectivo ese mismo día. *(Veremos esto en el caso práctico).*

---

## 3. Opciones: El Derecho, pero no la Obligación
Los Forwards y Futuros te obligan a ejecutar la compra, ganes o pierdas. Las **Opciones** son diferentes: te dan el *derecho* a comprar o vender, pero no la obligación. Para tener este lujo, debes pagar una prima (Premium) upfront.

* **Call (Opción de Compra):** Te da el derecho a **comprar** un activo a un precio preestablecido (Strike Price) antes de una fecha (Vencimiento).
  * Se compra cuando crees que el precio va a subir.
* **Put (Opción de Venta):** Te da el derecho a **vender** un activo a un precio preestablecido.
  * Se compra cuando crees que el precio va a bajar (o para proteger tu cartera de acciones).

> **💥 Impacto Financiero (Asimetría de Retornos):**
> * Si compras una acción a $100 y baja a $0, pierdes $100 (100%).
> * Si compras una Call con Strike a $100 pagando una prima de $5, y la acción baja a $0, solo pierdes $5. Tu pérdida máxima es la prima. Pero si la acción sube a $200, ganas $95 (apalancamiento brutal). Las opciones son el instrumento favorito de los Hedge Funds por esta asimetría matemática.
