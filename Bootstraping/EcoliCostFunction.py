import numpy as np
import matplotlib.pyplot as plt
import scipy.io as spio
from scipy.integrate import odeint
import EcoliEq as ode
#%matplotlib inline


def cost_function_Ecoli(vect, w, lsr, AI2, time):
#Cargar datos experimentales.
	# Define el vector de tiempo
	# pasos = 56
	#tiempo = np.linspace(0.0,12.0,pasos)
	# Xd_t = np.empty_like(tiempo)
	Ad_t = np.empty_like(time)
	Ld_t = np.empty_like(time)

	#Condiciones iniciales
	ci = [4.5, 0.0]
	Ad_t[0] = ci[0]
	Ld_t[0] = ci[1]

	# Resuelve el sistema de EDO paso a paso con un ciclo FOR
	for i in range(1,len(time)):
	    # Iniciamos el iterador en 1 porque el valor 0 ya lo definimos arriba
	    # Define el tamano del paso en el tiempo
	    tstep = [time[i-1],time[i]]
	    # Resuelve la ecuacion diferencial en el tiempo que abarca el paso
	    z = odeint(ode.QSEcoli,ci,tstep,args=(vect,))    
	    Ad_t[i] = z[1][0]
	    Ld_t[i] = z[1][1]
	    
	    ci = z[1]

	# Evaluacion de SSWR

	AI2_max = AI2[AI2.argmax()]
	lsr_max = lsr[lsr.argmax()]

	SSWR1 = sum(w * (((AI2 - Ad_t)/AI2_max)**2))
	SSWR2 = sum(w * (((lsr - Ld_t)/lsr_max)**2))

	SSWR = SSWR1 + SSWR2

	return SSWR

