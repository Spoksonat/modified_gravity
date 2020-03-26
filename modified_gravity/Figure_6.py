import numpy as np 
import matplotlib.pyplot as plt


# Codigo para hacer la gráfica 6 (Figure 6) del paper: https://arxiv.org/abs/2003.09006. 
# Esta grafica esta basada en las ecuaciones (3.47) y (3.48) y es una grafica parametrica de V contra phi (el parametro es y) para
# distintos valores de eta y p

# Funcion que permite calcular los valores de m y r dados los valores de y, eta y p
def valores_de_phi_y_V(y,eta,p):
    """
    phi= -np.sqrt(3.0/2.0)*np.log(1.0 - ((2**(-1.0/eta))*((eta*p)**(1.0+1.0/eta))*np.exp(2.0/(p*eta))*np.exp(-1.0/(y**eta)))/((2*p-2.0)*(y**(eta+1.0))))
    V_numerador = (2*(1.0/eta))*((p*eta)**(1.0/eta))*np.exp(2.0/(p*eta))*np.exp(1.0/(y**eta))*(p-1.0)*p*(y**2)*(1.0 - 1.0/(y**eta))
    V_denominador = ((p-1.0)*(2**(1.0+1.0/eta))*np.exp(1.0/(y**eta))*y - np.exp(2.0/(p*eta))*((p*eta)**(1.0 + 1.0/eta))-(1.0/(y**eta)))**2
    V = V_numerador/V_denominador
    """
    phi_eff = -np.sqrt(3.0/2.0)*np.log(1.0 - ((2**(-1.0/eta))*((eta*p)**(1.0+1.0/eta))*np.exp(2.0/(p*eta))*np.exp(-1.0/(y**eta)))/((2*p-2.0)*(y**(eta+1.0))))
    a = np.exp(-np.sqrt(2.0/3.0)*phi_eff)
    V_eff = (y*a*(2*p-2.0) - (2**(-1.0/eta))*p*((p*eta)**(1.0/eta))*np.exp(2.0/(p*eta))*np.exp(-1.0/(y**eta)))/((a**2)*(2*p-2.0))
    return phi_eff, V_eff

y = np.linspace(1.0,100,1000)

# Valores de phi y V para cada tupla de valores (eta,p) en la grafica
phi_20, V_20 = valores_de_phi_y_V(y,0.1,20.0)
phi_40, V_40 = valores_de_phi_y_V(y,0.05,40.0)
phi_100, V_100 = valores_de_phi_y_V(y,0.02,100.0)
phi_200, V_200 = valores_de_phi_y_V(y,0.01,200.0)



# Graficas de los valores de r y m junto con la linea de deSitter
plt.plot(phi_20,V_20,color ="#0000ff", linestyle='-', label=r"$(\eta=0.1,p=20)$")
plt.plot(phi_40,V_40,color ="#ff6600", linestyle='--', label=r"$(\eta=0.05,p=40)$")
plt.plot(phi_100,V_100,color ="#00802b", linestyle='-.',label=r"$(\eta=0.02,p=100)$")
plt.plot(phi_200,V_200,color ="#ff0000", linestyle=':', label=r"$(\eta=0.01,p=200)$")

plt.grid(b=True, linestyle='--')
plt.xlabel(r"$\phi/M_p$")
plt.ylabel(r"$2V/\mu^2 M_p$")
plt.legend()
plt.savefig("Figura_6.png")