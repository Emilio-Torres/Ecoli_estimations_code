import DifferentialEvolution as DE
import EcoliCostFunction as Ec
from time import time
import numpy as np
import random

# ------- Differential Evolution parameter setting -------- #
# Bounds 
b_kA = (500,1600)
b_m1 = (0.5,3)
b_n1 = (2,8)
b_Xd = (1,5.8211)
b_XA = (1,350)
b_m2 = (2, 5.8211)
b_n2 = (5,9)
b_LA = (0.0001,1)
b_kL = (0.01,9)
b_m3 = (0.01,6)
b_n3 = (0.0001,5)
b_AL = (0.0001,3)
b_kR = (0.001,3)

bounds = [b_kA,b_m1,b_n1,b_Xd,b_XA,b_m2,b_n2,b_LA,b_kL,b_m3,b_n3,b_AL,b_kR]
popsize = 60                        # Population size, must be >= 4
mutate = 0.2                        # Mutation factor [0,2]
recombination = 0.6                 # Recombination rate [0,1]
maxiter = 100						# Iteration number
cost_func = Ec.cost_function_Ecoli  # Cost function
# A list of initial values for parametres, empty if random parameters values
init_param =  [1348.5919872646969, 1.4134808360146387, 3.284591634007125, 5.795339289503388, 
99.99401097570676, 5.132789783520219, 8.452188718969653, 0.0032700106621533324, 
0.6046212696870696, 3.956508977030798, 0.0017229584039637046, 0.0028015141849171703, 0.12683595366855746] 
estimation_num = 500				# Bootstrap repetitions
file_name_1 = 'Bootstrap_SSWR.txt'	# File name
file_name_2 = 'Bootstrap_Parameters.txt'

start = time()
solutions = []
for i in range(0,estimation_num):
	w = np.random.exponential(1,56)
	solutions.append(DE.main(cost_func, bounds, popsize, mutate, recombination, maxiter, init_param, w))
	print('Estimation ',[i+1],' time :',(time() - start)/60, ' Min.')
	f = open(file_name_1,'a')
	f.write(str(solutions[i][0]) + '\n')
	f.close()
	f = open(file_name_2,'a')
	f.write(str(solutions[i][1]) + '\n')
	f.close()
print('Total procesing time :',(time() - start)/60, ' Min.')