# Importa las librerias de Python necesarias
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as spio
from scipy.integrate import odeint
import EcoliEq as ode
import math

# list with parameter values
vect = [1348.5919872646969, 1.4134808360146387, 3.284591634007125, 5.795339289503388, 
99.99401097570676, 5.132789783520219, 8.452188718969653, 0.0032700106621533324, 
0.6046212696870696, 3.956508977030798, 0.0017229584039637046, 0.0028015141849171703, 0.12683595366855746]

# Load experimental data
E_AI2 = spio.loadmat('ExpAI2.mat', squeeze_me=True)
E_lsr = spio.loadmat('Explsr.mat', squeeze_me=True)
E_cell = spio.loadmat('ExpCell.mat', squeeze_me=True)

AI2 = E_AI2['Exp_AI2']
lsr = E_lsr['Exp_lsr']
cell = E_cell['Exp_cell'] 

# time vector
steps = 1000
t = np.linspace(0.0,14.0,steps)
Ad_t = np.empty_like(t)
Ld_t = np.empty_like(t)

# Initial conditions
ci = [4.5, 0.0]
Ad_t[0] = ci[0]
Ld_t[0] = ci[1]

# Ode solver
for i in range(1,len(t)):
    tstep = [t[i-1],t[i]]
    # Resuelve la ecuacion diferencial en el tiempo que abarca el paso
    z = odeint(ode.QSEcoli,ci,tstep,args=(vect,))
    Ad_t[i] = z[1][0]
    Ld_t[i] = z[1][1]
    
    ci = z[1]

# Resuelve la funcion de crecimiento
x0 = 0.064
C = 5.8828 
B = 0.6384 
M = 3.2823

Xd_t = np.empty_like(t)
for i in range(len(Xd_t)):
	Xd_t[i] = x0 + C*math.exp(-math.exp(-B*(t[i]-M)))

# Graphics
font = {'fontsize':18}

plt.figure(figsize=(8,6))
fig1 = plt.subplot(3,1,1)
fig1.plot(t,Xd_t,label='Cellular growth')
fig1.plot(cell[:,0],cell[:,1],'o',label='Experimental data')
fig1.tick_params(axis='both',labelsize=16)
plt.ylabel('OD$_{600}$',fontdict=font)
#plt.xlabel('Tiempo')
fig1.legend(fontsize=16)
fig1.grid(True)

fig2 = plt.subplot(3,1,2)
fig2.plot(t,Ad_t,label='AI-2')
fig2.plot(AI2[:,0],AI2[:,1],'o',label='Experimental data')
fig2.tick_params(axis='both',labelsize=16)
plt.ylabel('Bioluminescence',fontdict=font)
#plt.xlabel('Tiempo')
fig2.legend(fontsize=16)
fig2.grid(True)

fig3 = plt.subplot(3,1,3)
fig3.plot(t,Ld_t,label='lsr Operon')
fig3.plot(lsr[:,0],lsr[:,1],'o',label='Experimental data')
fig3.tick_params(axis='both',labelsize=16)
plt.ylabel('Betagalactosidase',fontdict=font)
plt.xlabel('Time',fontdict=font)
fig3.legend(fontsize=16)
fig3.grid(True)

plt.show()