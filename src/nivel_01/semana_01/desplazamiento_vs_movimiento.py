import matplotlib.pyplot as plt
import numpy as np


# Colores a utilizar
color_demanda = '#1f77b4' # Azul
color_demanda_nueva = '#aec7e8' # Azul claro
color_oferta = '#d62728' # Rojo
color_oferta_nueva = '#ff9896' # Rojo claro
color_equilibrio = '#2ca02c' # Verde


def ejemplo_audifonos(axs):
    # =====================================================================
    # GRÁFICA 1: Desplazamiento de la Demanda (Ejemplo de los Audífonos)
    # =====================================================================
    ax1 = axs
    Q = np.linspace(0, 2500, 100)

    # Ecuaciones: P = mQ + b
    # Oferta (S): P = 0.1Q - 50
    # Demanda 1 (D1): P = -0.05Q + 100
    # Demanda 2 (D2): P = -0.05Q + 130
    S1 = 0.1 * Q - 50
    D1 = -0.05 * Q + 100
    D2 = -0.05 * Q + 130

    # Filtrar valores negativos para que las líneas no crucen los ejes
    S1 = np.where(S1 > 0, S1, np.nan)
    D1 = np.where(D1 > 0, D1, np.nan)
    D2 = np.where(D2 > 0, D2, np.nan)

    ax1.plot(Q, S1, color=color_oferta, label='Oferta (S)', linewidth=2)
    ax1.plot(Q, D1, color=color_demanda, label='Demanda Inicial (D1)', linewidth=2)
    ax1.plot(Q, D2, color=color_demanda_nueva, label='Demanda Nueva (D2)', linewidth=2, linestyle='--')

    # Puntos de equilibrio
    ax1.plot(1000, 50, 'go', ms=8) # E1
    ax1.plot(1200, 70, 'go', ms=8) # E2

    # Líneas punteadas hacia los ejes
    ax1.plot([1000, 1000], [0, 50], 'k--', lw=1)
    ax1.plot([0, 1000], [50, 50], 'k--', lw=1)
    ax1.plot([1200, 1200], [0, 70], 'k--', lw=1)
    ax1.plot([0, 1200], [70, 70], 'k--', lw=1)

    # Anotaciones
    ax1.annotate('Desplazamiento\n(por gusto/renta)', xy=(1000, 90), xytext=(1400, 110),
                arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8))
    ax1.text(1000, 40, 'E1', ha='center', color=color_equilibrio, fontweight='bold')
    ax1.text(1200, 60, 'E2', ha='center', color=color_equilibrio, fontweight='bold')

    ax1.set_title('Ej 1: Desplazamiento de Demanda\n(Mercado de Audífonos)')
    ax1.set_xlabel('Cantidad (Q)')
    ax1.set_ylabel('Precio (P)')
    ax1.set_xlim(0, 2500)
    ax1.set_ylim(0, 150)
    ax1.legend(loc='upper right')


def ejemplo_rosas(axs):
    # =====================================================================
        # GRÁFICA 2: Desplazamiento de la Oferta (Ejemplo de las Rosas)
        # =====================================================================
        ax2 = axs
        Q = np.linspace(0, 8000, 100)
    
        # Ecuaciones: P = mQ + b
        # Demanda (D): P = -0.003Q + 17
        # Oferta 1 (S1): P = 0.0005Q - 0.5
        # Oferta 2 (S2): P = 0.0005Q + 3
        D = -0.003 * Q + 17
        S1 = 0.0005 * Q - 0.5
        S2 = 0.0005 * Q + 3
    
        D = np.where(D > 0, D, np.nan)
        S1 = np.where(S1 > 0, S1, np.nan)
        S2 = np.where(S2 > 0, S2, np.nan)
    
        ax2.plot(Q, D, color=color_demanda, label='Demanda (D)', linewidth=2)
        ax2.plot(Q, S1, color=color_oferta, label='Oferta Inicial (S1)', linewidth=2)
        ax2.plot(Q, S2, color=color_oferta_nueva, label='Oferta Nueva (S2)', linewidth=2, linestyle='--')
    
        # Puntos de equilibrio
        ax2.plot(5000, 2, 'go', ms=8) # E1
        ax2.plot(4000, 5, 'go', ms=8) # E2
    
        # Líneas punteadas hacia los ejes
        ax2.plot([5000, 5000], [0, 2], 'k--', lw=1)
        ax2.plot([0, 5000], [2, 2], 'k--', lw=1)
        ax2.plot([4000, 4000], [0, 5], 'k--', lw=1)
        ax2.plot([0, 4000], [5, 5], 'k--', lw=1)
    
        # Anotaciones
        ax2.annotate('Desplazamiento\n(por costo/tiempo)', xy=(1500, 5), xytext=(2000, 8),
                    arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8))
        ax2.text(5000, 1.2, 'E1', ha='center', color=color_equilibrio, fontweight='bold')
        ax2.text(4000, 4.2, 'E2', ha='center', color=color_equilibrio, fontweight='bold')
    
        ax2.set_title('Ej 2: Desplazamiento de Oferta\n(Mercado de Rosas)')
        ax2.set_xlabel('Cantidad (Q)')
        ax2.set_ylabel('Precio (P)')
        ax2.set_xlim(0, 8000)
        ax2.set_ylim(0, 12)
        ax2.legend(loc='upper right')


def ejemplo_alquileres(axs):
    # =====================================================================
        # GRÁFICA 3: Movimiento puro - Precios Máximos (Ejemplo Alquileres)
        # =====================================================================
        ax3 = axs
        Q = np.linspace(0, 20000, 100)
    
        # Ecuaciones:
        # Demanda (D): P = -0.08Q + 1800
        # Oferta (S): P = 0.1Q
        D = -0.08 * Q + 1800
        S = 0.1 * Q
    
        D = np.where(D > 0, D, np.nan)
        S = np.where(S > 0, S, np.nan)
    
        ax3.plot(Q, D, color=color_demanda, label='Demanda (D)', linewidth=2)
        ax3.plot(Q, S, color=color_oferta, label='Oferta (S)', linewidth=2)
    
        # Punto de equilibrio inicial E1 (10000, 1000)
        ax3.plot(10000, 1000, 'go', ms=8)
    
        # Línea de precio máximo (Ceiling Price)
        ax3.axhline(y=600, color='purple', linestyle='-', linewidth=2, label='Precio Máximo ($600)')
    
        # Puntos de movimiento a lo largo de las curvas a P=600
        # Cantidad Ofrecida (Qs): 600 = 0.1Q -> Q = 6000
        # Cantidad Demandada (Qd): 600 = -0.08Q + 1800 -> 0.08Q = 1200 -> Q = 15000
        ax3.plot(6000, 600, 'ro', ms=8)
        ax3.plot(15000, 600, 'bo', ms=8)
    
        # Líneas de escasez
        ax3.plot([6000, 15000], [600, 600], color='orange', linewidth=5, alpha=0.5, label='Escasez (9000)')
    
        # Anotaciones
        ax3.text(10000, 920, 'E1 (Equilibrio)', ha='center', color=color_equilibrio, fontweight='bold')
        ax3.text(6500, 650, 'Mov. Oferta', color='red', fontweight='bold')
        ax3.text(14500, 650, 'Mov. Demanda', color='blue', fontweight='bold')
        ax3.annotate('Precio tope\nimpuesto', xy=(1000, 600), xytext=(3000, 300),
                    arrowprops=dict(facecolor='purple', shrink=0.05, width=1.5, headwidth=8))
    
        ax3.set_title('Ej 3: Movimiento puro por Precio Máximo\n(Mercado de Alquileres)')
        ax3.set_xlabel('Cantidad (Q)')
        ax3.set_ylabel('Precio (P)')
        ax3.set_xlim(0, 20000)
        ax3.set_ylim(0, 2000)
        ax3.legend(loc='upper right')


def ejemplos_dezplazamiento_movimientos():
    # Configuración general de las gráficas
    fig, axs = plt.subplots(1, 3, figsize=(25, 7))
    fig.suptitle('Diferencia entre Desplazamiento y Movimiento en el Equilibrio de Mercado', fontsize=16, fontweight='bold')

    ejemplo_audifonos(axs[0])
    ejemplo_rosas(axs[1])
    ejemplo_alquileres(axs[2])

    # Ajustar espaciado entre gráficas
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])

    # =====================================================================
    # GUARDAR EN ARCHIVO EN LUGAR DE MOSTRAR EN PANTALLA
    # =====================================================================
    nombre_archivo = 'equilibrio_mercado.png'
    plt.savefig(nombre_archivo, dpi=300, bbox_inches='tight')
    print(f"Gráfica guardada exitosamente como: {nombre_archivo}")


def save_fig_ejemplo_audifonos_dezplazamiento_movimientos(nombre_archivo = 'equilibrio_mercado_audifonos.png'):
    # Configuración general de las gráficas
    fig, axs = plt.subplots(1, 1, figsize=(10, 7))
    fig.suptitle('Diferencia entre Desplazamiento y Movimiento en el Equilibrio de Mercado', fontsize=16, fontweight='bold')

    ejemplo_audifonos(axs)

    # Ajustar espaciado entre gráficas
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig(nombre_archivo, dpi=300, bbox_inches='tight')
    print(f"Gráfica guardada exitosamente como: {nombre_archivo}")


def save_fig_ejemplo_rosas_dezplazamiento_movimientos(nombre_archivo = 'equilibrio_mercado_rosas.png'):
    # Configuración general de las gráficas
    fig, axs = plt.subplots(1, 1, figsize=(10, 7))
    fig.suptitle('Diferencia entre Desplazamiento y Movimiento en el Equilibrio de Mercado', fontsize=16, fontweight='bold')

    ejemplo_rosas(axs)

    # Ajustar espaciado entre gráficas
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig(nombre_archivo, dpi=300, bbox_inches='tight')
    print(f"Gráfica guardada exitosamente como: {nombre_archivo}")


def save_fig_ejemplo_alquileres_dezplazamiento_movimientos(nombre_archivo = 'equilibrio_mercado_alquileres.png'):
    # Configuración general de las gráficas
    fig, axs = plt.subplots(1, 1, figsize=(10, 7))
    fig.suptitle('Diferencia entre Desplazamiento y Movimiento en el Equilibrio de Mercado', fontsize=16, fontweight='bold')

    ejemplo_alquileres(axs)

    # Ajustar espaciado entre gráficas
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig(nombre_archivo, dpi=300, bbox_inches='tight')
    print(f"Gráfica guardada exitosamente como: {nombre_archivo}")


if __name__=='__main__':
    pass
    # ejemplos_dezplazamiento_movimientos()
    # save_fig_ejemplo_audifonos_dezplazamiento_movimientos()
    # save_fig_ejemplo_rosas_dezplazamiento_movimientos()
    # save_fig_ejemplo_alquileres_dezplazamiento_movimientos()