# Semana 12 · Sesión 4: Caso de Estudio y Evaluación

## 7. Análisis de Caso: El "Impuesto Inflacionario" y la trampa de los bonos largos

*Eres analista de renta fija en un fondo de pensiones. Hay una crisis mundial de suministros y la inflación global, que estaba en 2%, salta de golpe al 8%. El Banco Central reacciona subiendo la tasa de interés nominal del 4% al 11%.*

Tienes en el portafolio del fondo un Bono del Tesoro a 10 años que paga un cupón fijo del 4% nominal. El precio de mercado de ese bono hoy es de $100.

**Tu Análisis Matemático y Decision:**
1. **Tasa Real Negativa:** Antes, el inversor ganaba $4\% - 2\% = 2\%$ real. Hoy, si la inflación es 8% y el bono sigue pagando 4%, la **Tasa Real es** $(1.04 / 1.08) - 1 = -3.7\%$ anual real. Es una pérdida asegurada del poder adquisitivo.
2. **Ajuste de Mercado (Mark to Market):** Como ningún inversor racional querrá un bono que le da una tasa real negativa, todos venderán ese bono. Para que el bono sea atractivo, su precio debe caer drásticamente (ej. a $75) para que el "rendimiento al vencimiento" suba hacia el 11% (la nueva tasa nominal del mercado).
3. **Acción:** ¡Venta en pánico del bono de 10 años!迁移 a un bono "inflation-linked" (bono atado a la inflación, como los TIPS o el Udibono mexicano), donde el principal se ajusta por la inflación, garantizando matemáticamente una Tasa Real positiva sin importar lo que haga el IPC.

---

## 8. Tareas y Evaluación de la Semana 12

**A. Lectura Obligatoria:**
* Ross, Westerfield, Jordan. *Fundamentos de Finanzas Corporativas*. Capítulo 5 (Tasas de interés, inflación y equivalencia). 
* *Lecture complementaria:* Investopedia sobre el "Efecto Fisher".

**B. Preguntas de Reflexión:**
1. ¿Por qué la fórmula de la Tasa Real Aproximada ($r = i - h$) es peligrosa en países latinoamericanos con inflaciones superiores al 10% anual? Explica matemáticamente el "error" que se comete.
2. Si mañana announce que la inflación cae a 0% (deflación total o precios estables), ¿se dispararían o desplomarían las tasas nominales que ofrecen los bancos? ¿Por qué?

**C. Ejercicio Matemático a entregar:**
1. **Equivalencia de Tasas:** Tienes una tarjeta de crédito que cobra una Tasa Nominal Anual del 36% capitalizable mensualmente. El banco te ofrece refinanciarla a una Tasa Nominal Semestral. ¿Cuál debe ser exactamente la Tasa Nominal Semestral capitalizable trimestralmente ($m=2$) para que el préstamo sea matemáticamente equivalente? (Muestra tu fórmula y despeje).
2. **Ecuación de Fisher:** El gobierno emite un certificado de ahorro que paga una tasa nominal del 15% capitalizable mensual. La inflación anual proyectada es del 9%. Calcula:
   a) La Tasa Efectiva Anual (EAR) de este certificado.
   b) La Tasa Real Efectiva Anual usando la fórmula exacta de Fisher.

---
*¡Felicidades por completar la Semana 12! Ya nadie podrá engañarte con tasas de cartelera infladas por la capitalización o destruidas por la inflación. En la Semana 13 subiremos la dificultad: Series de Pagos (Anualidades, perpetuidades) y cómo se amortizan los préstamos.*