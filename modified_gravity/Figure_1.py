import numpy as np 
import matplotlib.pyplot as plt


# Codigo para hacer la gráfica 1 (Figure 1) del paper: https://arxiv.org/abs/2003.09006. 
# Esta grafica esta basada en la ecuacion (3.8) y es una grafica de m(r) contra r para r<-1.0 y
# distintos valores de eta
# Los cortes de la línea vertical con las demás se dan cuando m = 1-eta/2.0


# Linea del atractor de deSitter (r=-2)
r = -2.0*np.ones(1000)
m = np.linspace(0, 1.4 , 1000)
plt.plot(r,m,color ="#00b33c", linestyle='-')

# Vector de los posibles valores del parametro r
r = np.linspace(-2.4, -1.0 , 1000) # Vector de 1000 puntos que va desde -2.4 a -1.0

# Graficas de m(r) contra r para eta = 1/8 (linea azul)
eta = 1.0/8.0
m = -((r+1)*(r+eta))/r
plt.arrow(r[500], m[500], r[495]-r[500], m[495]-m[500], head_width=0.05, head_length=0.1, fc="#0000ff", ec="#0000ff")
plt.plot(r,m,color ="#0000ff", linestyle=':')
plt.plot(-2.0,1.0-eta/2.0,color ="#000000", marker='o') # Punto de interseccion con la linea vertical del atractor de deSitter

# Graficas de m(r) contra r para eta = 1/2 (linea naranja)
eta = 1.0/2.0
m = -((r+1)*(r+eta))/r
plt.arrow(r[500], m[500], r[495]-r[500], m[495]-m[500], head_width=0.05, head_length=0.1, fc="#ff6600", ec="#ff6600")
plt.plot(r,m,color ="#ff6600", linestyle='--') 
plt.plot(-2.0,1.0-eta/2.0,color ="#000000", marker='o') # Punto de interseccion con la linea vertical del atractor de deSitter

# Graficas de m(r) contra r para eta = 1 (linea verde oscuro discontinua)
eta = 1.0
m = -((r+1)*(r+eta))/r
plt.arrow(r[500], m[500], r[495]-r[500], m[495]-m[500], head_width=0.05, head_length=0.1, fc="#00802b", ec="#00802b")
plt.plot(r,m,color ="#00802b", linestyle='-.')
plt.plot(-2.0,1.0-eta/2.0,color ="#000000", marker='o') # Punto de interseccion con la linea vertical del atractor de deSitter

# Graficas de m(r) contra r para con m=-r-1 (linea negra)
m = -r-1
plt.plot(r,m,color ="#000000", linestyle='-')

# Graficas de m(r) contra r correspondiente a Lambda-CDM
m = np.zeros(len(r))
plt.plot(r,m,color ="#00ff00", linestyle='-')
plt.plot(-2.0,0.0,color ="#000000", marker='o') # Punto de interseccion con la linea vertical del atractor de deSitter

# Punto de silla P_M
plt.plot(-1.0,0.0,color ="#000000", marker='o') # Punto de interseccion con la linea vertical del atractor de deSitter

# Etiqueta de texto P_M
plt.text(-1.12,0.62, r"$P_M$", fontsize=15)
plt.arrow(-1.0,0.1,-1.07+1.0,0.5-0.1, head_width=0.04, head_length=0.1, fc="#00b33c", ec="#00b33c")

# Etiqueta de texto r = -2(de Sitter)
plt.text(-1.65,1.3, r"$r = -2$ (de Sitter)", fontsize=10)
plt.arrow(-1.95,1.31,0.15,0, head_width=0.04, head_length=0.1, fc="#00b33c", ec="#00b33c")

# Etiqueta de texto m = -r-1
plt.text(-1.3,0.9, r"$m= -r-1$", fontsize=10)
plt.arrow(-1.6+0.02,0.6+0.02,0.2-0.02,0.2-0.02, head_width=0.04, head_length=0.1, fc="#00b33c", ec="#00b33c")

# Etiqueta de texto 0<-R->infinito
plt.text(-1.71,0.09, r"$R$", fontsize=10)
plt.text(-1.94,0.09, r"$0$", fontsize=10)
plt.text(-1.49,0.09, r"$\infty$", fontsize=10)
plt.arrow(-1.65,0.1,0.05,0, head_width=0.04, head_length=0.1, fc="#00b33c", ec="#00b33c")
plt.arrow(-1.75,0.1,-0.05,0, head_width=0.04, head_length=0.1, fc="#00b33c", ec="#00b33c")

plt.grid(b=True, linestyle='--')
plt.xlabel(r"$r$")
plt.ylabel(r"$m(r)$")
plt.savefig("Figura_1.png")











