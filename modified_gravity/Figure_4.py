import numpy as np 
import matplotlib.pyplot as plt 
from scipy.special import lambertw

# Codigo para hacer la gráfica 4 (Figure 4) del paper: https://arxiv.org/abs/2003.09006. 
# Esta grafica esta basada en la ecuacion (3.23) y es una grafica de 2V/mu^2*M_p^2 contra phi/M_p par aeta = 3/5

# Definicion de parametros 
eta = 3.0/5.0 #valor de eta
phi_eff = np.linspace(0.0,2.0,1000) #Valor de phi_eff = phi/M_p

# Parametros que dependen de phi_eff y eta definidos para facilitar una mejor visualizacion del potencial en el codigo  
a = np.sqrt(2.0/3.0)*phi_eff 
b = 1.0/eta
c = -b-a
d = lambertw(-b*np.exp(c)) # Funcion W de Lambert

# Definicion del potencial efectivo V_eff = -2*V/M_p^2*mu^2  
V_eff = -(((np.exp(-a)-np.exp(b+d))*np.exp(2*a))/(-b-d)**(b))

# Grafica de V_eff
plt.plot(phi_eff,V_eff,color ="#0000ff", linestyle='-') # Graficar V_eff contra phi_eff
plt.xlabel(r"$\phi/M_p$") # Nombre del eje x
plt.ylabel(r"$-2V/\mu^2 M_p^2$") # Nombre del eje y
plt.grid(b=True, linestyle='--') # Activa grilla con lineas punteadas
plt.ylim(ymax=30) # Permite que el maximo en el eje y sea 30 (para que se aprezca a la grafica del paper)
plt.savefig("Figura_4.png")

