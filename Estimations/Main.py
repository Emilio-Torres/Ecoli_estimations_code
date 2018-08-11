import DifferentialEvolution as DE
import EcoliCostFunction as Ec
from time import time

# ------- Differential Evolution parameter setting -------- #
# Search space bounds for each parameter
b_kA = (500,1600)
b_m1 = (0.5,3)
b_n1 = (2,8)
b_Xd = (1,5.8211)
b_XA = (1,150)
b_m2 = (2, 5.8211)
b_n2 = (5,9)
b_LA = (0.0001,1)
b_kL = (0.01,9)
b_m3 = (0.01,6)
b_n3 = (0.0001,5)
b_AL = (0.0001,3)
b_kR = (0.001,3)

bounds = [b_kA,b_m1,b_n1,b_Xd,b_XA,b_m2,b_n2,b_LA,b_kL,b_m3,b_n3,b_AL,b_kR]#,b_gm]
popsize = 100                        # Population size, must be >= 4
mutate = 0.2                        # Mutation factor [0,2]
recombination = 0.6                 # Recombination rate [0,1]
maxiter = 20						# Iteration number
cost_func = Ec.cost_function_Ecoli  # Cost function
init_param = []						# A list with the initial parameter values, empty for random values
estimation_num = 1					# Estimation repetitions
file_name = 'Solutions.txt'			# File name

# --------- Run the differential evolution algorithm  --------- #
start = time()
solutions = []
for i in range(0,estimation_num):
	solutions.append(DE.main(cost_func, bounds, popsize, mutate, recombination, maxiter, init_param))
	print('Estimation ',[i+1],' time :',(time() - start)/60, ' Min.')
	f = open(file_name,'a')
	f.write(str(solutions[i][0]) + ' - ' + str(solutions[i][1])+'\n')
	f.close()
print('Total procesing time :',(time() - start)/60, ' Min.')