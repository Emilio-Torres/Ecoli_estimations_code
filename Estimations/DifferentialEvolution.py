import random
import EcoliCostFunction as Ec
import scipy.io as spio
from time import time
import numpy as np


def ensure_bounds(vec, bounds):
	vec_new = []
	#Cycle through each variable in vector
	for i in range(len(vec)):

		if vec[i] < bounds[i][0]:
			vec_new.append(bounds[i][0])
		if vec[i] > bounds[i][1]:
			vec_new.append(bounds[i][1])
		if bounds[i][0] <= vec[i] <= bounds[i][1]:
			vec_new.append(vec[i])

	return vec_new

def initializate_pop(popsize,bounds):
	random.seed()
	pop = []
	for i in range(0,popsize):						# range(1,popsize)
		indv = []
		for j in range(len(bounds)):
			indv.append(random.uniform(bounds[j][0],bounds[j][1]))
		pop.append(indv)
	return pop

def main(cost_func, bounds, popsize, mutate, recombination, maxiter, init_param):

	# Load the experimental data
	Exp = spio.loadmat('interpolate_data.mat', squeeze_me=True)
	AI2 = np.array(Exp['AI2_interp'])
	lsr = np.array(Exp['lsr_interp'])
	t = np.array(Exp['time_interp'])
	
	cont = 0
	best = [] 		# return the best solution and member

	# Initialize a population 
	population = initializate_pop(popsize,bounds)		
	# If there is an initial set of parameter values
	if len(init_param) != 0:
		init_value = init_param
		population[0] = init_value
	else:
		init_value = population[0]

	# List for save the best value and member of each generation.
	gen_sol = []
	gen_mem = []
	best_sol = cost_func(init_value,AI2,lsr,t)
	best_mem = init_value
	gen_sol.append(best_sol)
	gen_mem.append(best_mem)
	
	#-- Solve --
		# Cycle through each generation 
	for i in range(1,maxiter+1):

		if cont == 20:
			population = initializate_pop(popsize,bounds)
			population[0] = best_mem
			print("population reinizializated")
			cont = 0

		# Cycle through each individuaol in the population 
		# Mutation strategy DE/best/1
		for j in range(0,popsize):
			
			cand = list(range(0,popsize))
			cand.remove(j)
			random_index = random.sample(cand,2)

			x_1 = best_mem 					# The best individual
			x_2 = population[random_index[0]]	# Two random individual
			x_3 = population[random_index[1]]	#  			
			x_t = population[j] 				# Current individual

			x_diff = [x_2_i - x_3_i for x_2_i, x_3_i in zip(x_2, x_3)]
			v_mutant = [x_1_i + mutate * x_diff_i for x_1_i, x_diff_i in zip(x_1, x_diff)]
			v_mutant = ensure_bounds(v_mutant,bounds) 

		    # Recombination
			v_trial = []
		    # cycle through each variable in our target vector
		    # Recombination strategy DE/best/1/exp
			for k in range(len(x_t)):
				crossover = random.random()
				if crossover <= recombination:
					v_trial.append(v_mutant[k])
				else:
					v_trial.append(x_t[k])

	        # Selection
			score_trial  = cost_func(v_trial,AI2,lsr,t)
			score_target = cost_func(x_t,AI2,lsr,t)

			if score_trial < score_target:
				population[j] = v_trial
				if score_trial < best_sol:
					best_mem = v_trial
					best_sol = score_trial
	    
		# Fitness of best individual
		gen_sol.append(best_sol)            
		# Best member
		gen_mem.append(best_mem)

		print ('> Generation: ', i)
		print ('> Best solution: ',best_sol)
		print ('> Best generation individual: ',best_mem,'\n')

		# Count the generations without enhance the solution
		if gen_sol[i-1] == gen_sol[i]:
			cont = cont+1
		else:
			cont = 0

	print ('      > BEST GLOBAL SOLUTION:',best_sol)
	print ('      > BEST GLOBAL INDIVIDUAL:',best_mem,'\n')
	
	best.append(best_sol)
	best.append(best_mem)	
	return best


