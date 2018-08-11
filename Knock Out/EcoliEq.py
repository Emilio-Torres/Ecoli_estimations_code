from math import exp

#Definir las ecuaciones diferenciales

def QSEcoli(initial_cond, t, param):
    
    #Condiciones iniciales
    A = initial_cond[0]
    L = initial_cond[1]
    
    # Constants
    k_A     = 1561.6802
    k_m1    = param[0]
    n1      = 2.9302
    # X_d     = 5.818496720128825
    k_XA    = param[1]
    k_m2    = 5.8205
    n2      = 8.9542
    # k_LA    = param[7]
    
    k_L     = param[2]
    k_m3    = param[3]
    n3      = 0.0017229584039637046
    # k_AL    = param[11]
    k_R     = param[4]
    
    x0 = 0.064
    C = 5.8828 
    B = 0.6384 
    M = 3.2823

    # Gompertz function for baterial growth
    X = x0 + C*exp(-exp(-B*(t-M)))

    # ODEs
    
    # Extracellular concentration
    mu_A    = k_A * (X**n1/(X**n1 + k_m1**n1))
    mu_XA   = k_XA * (X**n2/(X**n2 + k_m2**n2)) * A
    mu_LA   = 0     #k_LA * A * L * (X/X_d)
    dAdt    = mu_A - mu_XA - mu_LA 

    # Operon expression
    mu_L    = k_L * (X**n3/(X**n3 + k_m3**n3)) * A 
    mu_AL   = 0     #k_AL *  A * L * (X/X_d)
    mu_R    = k_R * L
    dLdt    = mu_L + mu_AL - mu_R
    
    return [dAdt,dLdt]