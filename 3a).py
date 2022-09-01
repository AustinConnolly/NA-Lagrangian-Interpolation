# Numerical Problems in assignmnent 2 Question 3
# CNNAUA001
# 4/6/2020

## Importing Libraries -------------------------------------------------------------------------------------------------
import numpy as np
import scipy as sc
import matplotlib.pyplot  as plt
from matplotlib import rc
##----------------------------------------------------------------------------------------------------------------------

## Defining Interpolating Polynomial -----------------------------------------------------------------------------------
def p(x):
    y = ((x**3)/np.pi**3)*(90-54*np.sqrt(3)) + ((x**2)/np.pi**2)*(-63+36*np.sqrt(3)) + ((x)/np.pi)*((22-9*np.sqrt(3))/2)
    return y
##----------------------------------------------------------------------------------------------------------------------

## Initialising Variables and Arrays -----------------------------------------------------------------------------------
x=np.linspace(0,2*np.pi,1000) # Array of x-values for 0 to 2\pi
x=np.linspace(0,0.5*np.pi,1000) # Array of x-values for 0 to 0.5*\pi
##----------------------------------------------------------------------------------------------------------------------

## Plotting ------------------------------------------------------------------------------------------------------------
plt.plot(x,p(x),'-g',label='Approximation of $\sin x$') # Plots approximation p(x)
plt.plot(x,np.sin(x),'-r',label='$\sin x$') # Plots sin(x)
plt.plot(x,p(x)-np.sin(x),label='Difference between $p(x)$ and $\sinx$') # Plots difference between p(x) and sin(x)
plt.tick_params(direction='in',top=True,right=True) 
plt.xlabel('x') 
plt.ylabel('y')
plt.legend() 
##----------------------------------------------------------------------------------------------------------------------