import numpy as np
import matplotlib.pyplot as plt
import scipy.io as spio
from scipy.integrate import odeint
import EcoliEq as ode

def cost_function_Ecoli(vect,AI2,lsr,time):

	Ad_t = np.empty_like(time)
	Ld_t = np.empty_like(time)

	# Initial condition
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

	# Evaluation of SSWR

	AI2_max = AI2[AI2.argmax()]
	lsr_max = lsr[lsr.argmax()]

	SSWR1 = sum(((AI2 - Ad_t)/AI2_max)**2)
	SSWR2 = sum(((lsr - Ld_t)/lsr_max)**2)

	SSWR = SSWR1 + SSWR2

	return SSWR

