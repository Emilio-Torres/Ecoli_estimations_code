from math import exp

#Definir las ecuaciones diferenciales

def QSEcoli(initial_cond, t, param):
    
    #Initial conditions
    A = initial_cond[0]
    L = initial_cond[1]
    
    # Constants
        
    k_A     = param[0]
    k_m1    = param[1]
    n1      = param[2]
    X_d     = param[3]
    k_XA    = param[4]
    k_m2    = param[5]
    n2      = param[6]
    k_LA    = param[7]
    
    k_L     = param[8]
    k_m3    = param[9]
    n3      = param[10]
    k_AL    = param[11]
    k_R     = param[12]

    x0 = 0.064
    C = 5.8828 
    B = 0.6384 
    M = 3.2823

    #Gompertz function for baterial growth
    X = x0 + C*exp(-exp(-B*(t-M)))

    # ODEs
    
    # Extracellular concentration
    mu_A    = k_A * (X**n1/(X**n1 + k_m1**n1))
    mu_XA   = k_XA * (X**n2/(X**n2 + k_m2**n2)) * A
    mu_LA   = k_LA * A * L * (X/X_d)
    dAdt    = mu_A - mu_XA - mu_LA 

    # Operon expression
    mu_L    = k_L * (X**n3/(X**n3 + k_m3**n3)) * A 
    mu_AL   = k_AL *  A * L * (X/X_d)
    mu_R    = k_R * L
    dLdt    = mu_L + mu_AL - mu_R
    
    return [dAdt,dLdt]