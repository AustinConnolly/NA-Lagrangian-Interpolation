# Numerical Problems in assignmnent 2 Question 3
# CNNAUA001
# 4/6/2020

## Importing Libraries -------------------------------------------------------------------------------------------------
import numpy as np
import scipy as sc
import matplotlib.pyplot  as plt
from matplotlib import rc
##----------------------------------------------------------------------------------------------------------------------

## Defining L0(x) ------------------------------------------------------------------------------------------------------
def L0(x):
    y = -(36/np.pi**3)*x**3 + (36/np.pi**2)*x**2-(11/np.pi)*x +1
    return y
##----------------------------------------------------------------------------------------------------------------------

## Defining L1(x) ------------------------------------------------------------------------------------------------------
def L1(x):
    y = (108/np.pi**3)*x**3 - (90/np.pi**2)*x**2+(18/np.pi)*x 
    return y
##----------------------------------------------------------------------------------------------------------------------

## Defining L2(x) ------------------------------------------------------------------------------------------------------
def L2(x):
    y = -(108/np.pi**3)*x**3 + (72/np.pi**2)*x**2-(9/np.pi)*x 
    return y
##----------------------------------------------------------------------------------------------------------------------

## Defining L3(x) ------------------------------------------------------------------------------------------------------
def L3(x):
    y = (36/np.pi**3)*x**3 - (18/np.pi**2)*x**2 + (2/np.pi)*x 
    return y
##----------------------------------------------------------------------------------------------------------------------

## Initialising Variables and Arrays -----------------------------------------------------------------------------------
x=np.linspace(0,0.5*np.pi,1000) # Array of x-values for 0 to 0.5*\pi
##----------------------------------------------------------------------------------------------------------------------

## Plotting ------------------------------------------------------------------------------------------------------------
plt.plot(x,L0(x),label='$L_0(x)$') # Plots L1(x)
plt.plot(x,L1(x),label='$L_1(x)$') # Plots L2(x)
plt.plot(x,L2(x),label='$L_2(x)$') # Plots L3(x)
plt.plot(x,L3(x),label='$L_3(x)$') # Plots L4(x)
plt.tick_params(direction='in',top=True,right=True) 
plt.xlabel('x') 
plt.ylabel('y')
plt.legend() 
##----------------------------------------------------------------------------------------------------------------------