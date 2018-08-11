import DifferentialEvolution as DE
import EcoliCostFunction as Ec
from time import time

# ------- Differential Evolution parameter setting -------- #
# Bounds 
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


vectors = []
vectors.append([800, 1000, 1300, 1330, 1340, 1345, 1348, 1348.5, 1348.5914, 1348.6, 1349, 1350, 1360, 1380, 1400, 1500, 2000]) #kA
vectors.append([0.01, 0.1, 1, 1.3, 1.41, 1.412, 1.4125, 1.4130, 1.4134, 1.4135, 1.414, 1.415, 1.42, 1.50, 2, 5, 10]) #km1
vectors.append([0.1, 2, 3, 3.2, 3.28, 3.282, 3.283, 3.284, 3.2845, 3.285, 3.286, 3.287, 3.29, 3.3, 3.5, 4, 10]) #n1
vectors.append([0.1, 1, 5, 5.6, 5.7, 5.793, 5.794, 5.795, 5.7953, 5.7955, 5.796, 5.797, 5.8, 5.9, 6, 10, 20]) #Xd
vectors.append([1, 10, 50, 90, 98, 99, 99.99, 99.993, 99.994, 99.9945, 99.995, 100, 101, 110, 150, 200, 400]) #kXA
vectors.append([0.1, 1, 4, 5, 5.1, 5.13, 5.132, 5.1325, 5.1327, 5.133, 5.134, 5.14, 5.15, 5.5, 6, 10, 20]) #km2
vectors.append([0.1, 1, 5, 7, 8, 8.4, 8.45, 8.452, 8.4521, 8.4525, 8.453, 8.455, 8.46, 8.5, 9, 10, 20]) #n2
vectors.append([1e-5, 5e-5, 1e-4, 5e-4, 1e-3, 3e-3, 3.2e-3, 3.25e-3, 3.27e-3, 3.28e-3, 3.3e-3, 3.5e-3, 5e-3, 0.01, 0.1, 1, 5]) #kLA
vectors.append([0.01, 0.05, 0.1, 0.5, 0.6, 0.603, 0.604, 0.6046, 0.60462, 0.60465, 0.6047, 0.605, 0.61, 0.65, 0.7, 1, 5]) #kL
vectors.append([0.1, 0.5, 1, 3, 3.5, 3.95, 3.958, 3.968, 3.9685, 3.9695, 4, 5, 10, 20]) #km3
vectors.append([1e-5, 5e-5, 1e-4, 5e-4, 1e-3, 1.5e-3, 1.7e-3, 1.72e-3, 1.722e-3, 1.725e-3, 1.73e-3, 1.8e-3, 2e-3, 0.01, 0.1, 1, 5]) #n3
vectors.append([1e-5, 5e-5, 1e-4, 5e-4, 1e-3, 2e-3, 2.5e-3, 2.8e-3, 2.801e-3, 2.805e-3, 2.81e-3, 2.85e-3, 3e-3, 0.01, 0.1, 1, 5]) #kAL
vectors.append([0.001, 0.01, 0.05, 0.1, 0.12, 0.126, 0.1268, 0.12683, 0.126835, 0.12684, 0.12685, 0.1269, 0.127, 0.13, 0.2, 1, 5]) #kR

bounds = [b_kA,b_m1,b_n1,b_Xd,b_XA,b_m2,b_n2,b_LA,b_kL,b_m3,b_n3,b_AL,b_kR]
popsize = 60                        # Population size, must be >= 4
mutate = 0.5                        # Mutation factor [0,2]
recombination = 0.7                 # Recombination rate [0,1]
maxiter = 200						# Iteration number
cost_func = Ec.cost_function_Ecoli  # Cost function
init_param = [1348.5919872646969, 1.4134808360146387, 3.284591634007125, 5.795339289503388, 
99.99401097570676, 5.132789783520219, 8.452188718969653, 0.0032700106621533324, 0.6046212696870696, 
3.956508977030798, 0.0017229584039637046, 0.0028015141849171703, 0.12683595366855746] # A list with the initial parameter values, empty for random values
file_name = 'Likelihood_solutions.txt' # File name

start = time()
for j in range(0,len(vectors)):
	vector = vectors[j]
	f = open(file_name,'a')
	f.write('\n')
	f.close()
	for i in range(0,len(vector)):
		data = (j,vector[i])
		sol = (DE.main(cost_func, bounds, popsize, mutate, recombination, maxiter, init_param, data))
		print('Estimation ',[i+1],' time :',(time() - start)/60, ' Min.')
		f = open(file_name,'a')
		f.write(str(sol) + ', ')
		f.close()
print('Total procesing time :',(time() - start)/60, ' Min.')