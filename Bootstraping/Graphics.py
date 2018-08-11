import numpy as np
import scipy.io as spio
import matplotlib.pyplot as plt

data = open('Bootstrap_Parameters.txt','r')# 
f = open('temp.txt','w')
parameter = []
line = ''
while True: 
    char = data.read(1)  # lee caracter
    if char != '[':
        if char !=']':
            line = line+char
            if char == '\n':
                f.write(line)
                line = ''
    if not char:
        break
data.close()  
f.close()

Params = np.loadtxt('temp.txt',delimiter=',',skiprows=0)
error = np.loadtxt('Bootstrap_SSWR.txt',delimiter=',',skiprows=0)
bounds = ['k$_{A}$','k$_{m1}$','n$_{1}$','X$_\delta$','k$_{XA}$','k$_{m2}$','n$_{2}$','k$_{LA}$','k$_{L}$','k$_{m3}$','n$_{3}$','k$_{AL}$','k$_{R}$']

# Compute the 95% confidence interval
r = []
font = {'fontsize':10}
for i in range(0,13):
    p = np.empty_like(error)
    for j in range(0,len(error)):
        p[j] = Params[j][i]
    np.sort(p)
    r.append(p[14:522])
    
# histogram 
for i in range(0,13):
    plt.figure(1)
    fig = plt.subplot(5,3,i+1)
    fig.tick_params(axis='both',labelsize=8)
    plt.ylabel('Frequency',fontdict=font)
    plt.xlabel(bounds[i],fontdict=font)
    plt.hist(r[i],50)

# Scatter graphics
k = 2
m = 1
for i in range(1,13):
#for i in range(0,1):
    for j in range(0,i):
    #for j in range(0,13):
        plt.figure(k)
        fig = plt.subplot(8,3,m)
        fig.tick_params(axis='both',labelsize=8)
        #plt.ylabel(bounds[i])
        plt.ylabel(bounds[i],fontdict=font)
        plt.xlabel(bounds[j],fontdict=font)
        plt.scatter(r[j],r[i],s=1,marker='.')
        m += 1
        if m % 25 == 0:
            m = 1
            k += 1            
plt.show()

