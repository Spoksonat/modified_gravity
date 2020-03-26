import numpy as np 
import matplotlib.pyplot as plt


# Codigo para hacer la gráfica 5 (Figure 5) del paper: https://arxiv.org/abs/2003.09006. 
# Esta grafica esta basada en las ecuaciones (3.45) y (3.46) y es una grafica parametrica de m contra r (el parametro es y) para
# distintos valores de eta y p
# Los cortes de la línea vertical con las demás se dan cuando r = -2

# Funcion que permite calcular los valores de m y r dados los valores de y, eta y p
def valores_de_r_y_m(y,eta,p):
    r_numerador = (2.0**(1.0 + 1.0/eta))*(p-1.0)*y*np.exp(1.0/(y**eta)) - ((p*eta)**(1.0 + 1.0/eta))*np.exp(2.0/(p*eta))*(1.0/y**eta)
    r_denominador = (2.0**(1.0 + 1.0/eta))*(p-1.0)*y*np.exp(1.0/(y**eta)) - (p*(p*eta)**(1.0/eta))*np.exp(2.0/(p*eta))
    r = -r_numerador/r_denominador
    m_numerador = eta*((p*eta)**(1.0/eta))*np.exp(2.0/(p*eta))*(1.0/(y**eta))*(1.0 + eta*(1.0-(1.0/(y**eta))))
    m_denominador = (2.0**(1.0/eta))*(2.0 - (2.0/p))*y*np.exp(1.0/(y**eta)) - eta*((p*eta)**(1.0/eta))*np.exp(2.0/(p*eta))*(1.0/(y**eta))
    m = m_numerador/m_denominador
    return r,m

y = np.linspace(1.0,100,1000)

# Valores de r y m para cada tupla de valores (r,m) en la grafica
r_20, m_20 = valores_de_r_y_m(y,0.1,20.0)
r_40, m_40 = valores_de_r_y_m(y,0.05,40.0)
r_100, m_100 = valores_de_r_y_m(y,0.02,100.0)
r_200, m_200 = valores_de_r_y_m(y,0.01,200.0)

# Linea del atractor de deSitter (r=-2)
r_deSitter = -2.0*np.ones(1000)
m_deSitter = np.linspace(0,np.amax(m_20), 1000)


# Graficas de los valores de r y m junto con la linea de deSitter
plt.plot(r_deSitter,m_deSitter,color ="#ac3973", linestyle='-', label="de Sitter")
plt.plot(r_20,m_20,color ="#0000ff", linestyle='-', label=r"$(\eta=0.1,p=20)$")
plt.plot(r_40,m_40,color ="#ff6600", linestyle='--', label=r"$(\eta=0.05,p=40)$")
plt.plot(r_100,m_100,color ="#00802b", linestyle='-.',label=r"$(\eta=0.02,p=100)$")
plt.plot(r_200,m_200,color ="#ff0000", linestyle=':', label=r"$(\eta=0.01,p=200)$")


# Punto de silla P_M
plt.plot(-1.0,0.0,color ="#000000", marker='o', label=r"$P_M$") # Punto de interseccion con la linea vertical del atractor de deSitter

plt.grid(b=True, linestyle='--')
plt.xlabel(r"$r$")
plt.ylabel(r"$m(r)$")
plt.legend()
plt.savefig("Figura_5.png")




