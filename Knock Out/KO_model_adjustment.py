# Importa las librerias de Python necesarias
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as spio
from scipy.integrate import odeint
import EcoliEq as ode
import math

# Vector values for adjust knockout model
#  		[k_m1	k_XA 	k_L 	k_m3	k_R]
vect = [2.8673785876300983, 19.792125757969284, 15.79001499848276, 0.0005250739517017472, 250.0]

# Experimental data
Exp = spio.loadmat('KOAI2.mat', squeeze_me=True)
Exp1 = spio.loadmat('KOlsr.mat', squeeze_me=True)
AI2 = np.array(Exp['KnockOut_AI2'])
lsr = np.array(Exp1['KnockOut_lsr'])

# time vector
step = 1000
time = np.linspace(0.0,12.0,step)
Ad_t = np.empty_like(time)
Ld_t = np.empty_like(time)

# Initial conditions
ci = [4.5, 0.0]
Ad_t[0] = ci[0]
Ld_t[0] = ci[1]

# Ode solver
for i in range(1,len(time)):
    tstep = [time[i-1],time[i]]
    z = odeint(ode.QSEcoli,ci,tstep,args=(vect,))    
    Ad_t[i] = z[1][0]
    Ld_t[i] = z[1][1]
    
    ci = z[1]

# Solve Gompertz function
x0 = 0.064
C = 5.8828 
B = 0.6384 
M = 3.2823

Xd_t = np.empty_like(time)
for i in range(len(Xd_t)):
	Xd_t[i] = x0 + C*math.exp(-math.exp(-B*(time[i]-M)))

# Graphics
font = {'fontsize':18}
plt.figure(1)

fig2 = plt.subplot(2,1,1)
fig2.plot(time,Ad_t,label='AI-2')
fig2.plot(AI2[:,0],AI2[:,1],'o',label='Experimental data')
fig2.tick_params(axis='both',labelsize=16)
plt.ylabel('OD$_{490}$',fontdict=font)
fig2.legend(fontsize=16)
fig2.grid(True)

fig3 = plt.subplot(2,1,2)
fig3.plot(time,Ld_t,label='lsr Operon')
fig3.plot(lsr[:,0],lsr[:,1],'o',label='Experimental data')
fig3.tick_params(axis='both',labelsize=16)
plt.ylabel(r'$\beta$-galactosidase',fontdict=font)
plt.xlabel('Time',fontdict=font)
fig3.legend(fontsize=16)
fig3.grid(True)

plt.show()