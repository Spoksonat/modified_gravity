import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

N_min = -9.0#-5.0
N_max = 3.0
n_puntos = 100
h = (N_max - N_min)/n_puntos
eta = 0.68


def x_prima(x,y,z,w):
    return x**2 - x*z - 3*y - z + w - 1.0


def y_prima(x,y,z,w):
    m = -0.0361869+ 0.0533559*np.sqrt(np.abs(z/y)) + 0.0171674*(z/y)
    return x*y + x*z/m - 2*y*(z-2.0)
   

def z_prima(x,y,z,w):
    m = -0.0361869+ 0.0533559*np.sqrt(np.abs(z/y)) + 0.0171674*(z/y)
    return -x*z/m - 2*z*(z-2.0)
    

def w_prima(x,y,z,w):
   return x*w - 2*z*w

def sol(N_0,x_0,y_0,z_0,w_0):
    N = np.zeros(n_puntos)
    x = np.zeros(n_puntos) 
    y = np.zeros(n_puntos)
    z = np.zeros(n_puntos)
    w = np.zeros(n_puntos)
    
    #Condiciones iniciales
    x[0] = x_0#0.0
    y[0] = y_0#-0.5
    z[0] = z_0#0.500248999599696542179
    w[0] = w_0#0.05
    N[0] = N_0#N_min
    #print(N[0],x[0],y[0],z[0],w[0])
    # Inicia Runge Kutta Orden 4
    for i in range(1,n_puntos):
        k1_x = h * x_prima(x[i-1],y[i-1],z[i-1],w[i-1]) #Euler
        k1_y = h * y_prima(x[i-1],y[i-1],z[i-1],w[i-1])
        k1_z = h * z_prima(x[i-1],y[i-1],z[i-1],w[i-1])
        k1_w = h * w_prima(x[i-1],y[i-1],z[i-1],w[i-1])
        

        k2_x = h * x_prima(x[i-1] + 0.5*k1_x, y[i-1] + 0.5*k1_y, z[i-1]+ 0.5*k1_z,w[i-1] + 0.5*k1_w ) # h*f'(t + 0.5*h, x + 0.5*k1, y) 
        k2_y = h * y_prima(x[i-1] + 0.5*k1_x, y[i-1] + 0.5*k1_y, z[i-1]+ 0.5*k1_z,w[i-1] + 0.5*k1_w )# h*f'(t + 0.5*h, x, y + 0.5*k1)
        k2_z = h * z_prima(x[i-1] + 0.5*k1_x, y[i-1] + 0.5*k1_y, z[i-1]+ 0.5*k1_z,w[i-1] + 0.5*k1_w )
        k2_w = h * w_prima(x[i-1] + 0.5*k1_x, y[i-1] + 0.5*k1_y, z[i-1]+ 0.5*k1_z,w[i-1] + 0.5*k1_w )
       


        k3_x = h * x_prima(x[i-1] + 0.5*k2_x, y[i-1] + 0.5*k2_y, z[i-1]+ 0.5*k2_z,w[i-1] + 0.5*k2_w ) # h*f'(t + 0.5*h, x + 0.5*k2, y) 
        k3_y = h * y_prima(x[i-1] + 0.5*k2_x, y[i-1] + 0.5*k2_y, z[i-1]+ 0.5*k2_z,w[i-1] + 0.5*k2_w )# h*f'(t + 0.5*h, x, y + 0.5*k2)
        k3_z = h * z_prima(x[i-1] + 0.5*k2_x, y[i-1] + 0.5*k2_y, z[i-1]+ 0.5*k2_z,w[i-1] + 0.5*k2_w )
        k3_w = h * w_prima(x[i-1] + 0.5*k2_x, y[i-1] + 0.5*k2_y, z[i-1]+ 0.5*k2_z,w[i-1] + 0.5*k2_w )
        


        k4_x = h * x_prima(x[i-1] + k3_x, y[i-1] + k3_y, z[i-1] + k3_z, w[i-1] + k3_w ) # h*f'(t + 0.5*h, x + k3, y) 
        k4_y = h * y_prima(x[i-1] + k3_x, y[i-1] + k3_y, z[i-1] + k3_z, w[i-1] + k3_w )# h*f'(t + 0.5*h, x, y + k3)
        k4_z = h * z_prima(x[i-1] + k3_x, y[i-1] + k3_y, z[i-1] + k3_z, w[i-1] + k3_w )
        k4_w = h * w_prima(x[i-1] + k3_x, y[i-1] + k3_y, z[i-1] + k3_z, w[i-1] + k3_w )
        

    #Promedio ponderado de pendientes
        average_k_x = (1.0/6.0)*(k1_x + 2.0*k2_x + 2.0*k3_x + k4_x)
        average_k_y = (1.0/6.0)*(k1_y + 2.0*k2_y + 2.0*k3_y + k4_y)
        average_k_z = (1.0/6.0)*(k1_z + 2.0*k2_z + 2.0*k3_z + k4_z)
        average_k_w = (1.0/6.0)*(k1_w + 2.0*k2_w + 2.0*k3_w + k4_w)
    # Evolucion en el tiempo
        N[i] = N[i-1] + h
        x[i] = x[i-1] + average_k_x
        y[i] = y[i-1] + average_k_y 
        z[i] = z[i-1] + average_k_z 
        w[i] = w[i-1] + average_k_w 
        #print(N[i],x[i],y[i],z[i],w[i])
    # Termina Runge Kutta Orden 4
    return N,x,y,z,w

y_0 = np.linspace(-1.0,0.0,1000000)
z_0 = np.linspace(0.06,0.08,100000)

for j in z_0:
    N,x,y,z,w = sol(N_min,0.0,-0.07,j,0.9)   
    Omega_DE = x + y + z
    Omega_rad = w
    Omega_m = 1.0 - Omega_DE - Omega_rad
    if(np.amax(Omega_m)> 0.4):
        print("maximo:",np.amax(Omega_m),j)



"""
Omega_DE = x + y + z
Omega_rad = w
Omega_m = 1.0 - Omega_DE - Omega_rad


x_ceros = np.zeros(1000)
y_ceros = np.linspace(0.0, 1.0 , 1000)


plt.plot(N,Omega_rad,color ="#00b33c", linestyle='-.', label=r"$\Omega_r$")
plt.plot(N,Omega_m,color ="#ff6600", linestyle='--', label=r"$\Omega_m$")
plt.plot(N,Omega_DE,color ="#0000ff", linestyle=':', label=r"$\Omega_{DE}$")
plt.plot(x_ceros,y_ceros,color ="#bfbfbf", linestyle='-')
plt.grid(b=True, linestyle='--')
plt.xlabel(r"$-\ln(1+z)$")
plt.xlabel(r"$\Omega$")
plt.legend()
plt.savefig("Figura_7.png")
plt.clf()

W_eff = -(1.0/3.0)*(2*z-1.0)
W_DM =  -(1.0/3.0)*(2*z - 1.0 + w)/(x + y + z)

y_ceros_n = np.linspace(-1.0, 0.0 , 1000)

plt.plot(N[int(n_puntos/2.0):],W_eff[int(n_puntos/2.0):],color ="#ff6600", linestyle='--', label=r"$w_{eff}$")
plt.plot(N[int(n_puntos/2.0):],W_DM[int(n_puntos/2.0):],color ="#0000ff", linestyle=':', label=r"$w_{DM}$")
plt.plot(x_ceros,y_ceros_n,color ="#bfbfbf", linestyle='-')
plt.grid(b=True, linestyle='--')
plt.xlabel(r"$-\ln(1+z)$")
plt.ylabel(r"$w_{eff},w_{DE}$")
plt.legend()
plt.savefig("Figura_8.png")
"""