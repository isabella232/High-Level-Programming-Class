from math import sin
import math
import numpy as np

from integrator import integrate
from numpy_integrator import numpy_integrate
from numba_integrator import numba_integrate
from cython_integrator import cython_integrate

from integrator import midpoint_integrate
from numpy_integrator import numpy_midpoint_integrate
from numba_integrator import numba_midpoint_integrate
from cython_integrator import cython_midpoint_integrate

def f5(x):
	return np.sin(x)


approx=0
i=1
while abs(approx-float(2.0)) > 10e-10:
#for i in range(1,10):
	#print ("here",i,integrate(f5,0, math.pi,i*1000))
	approx=integrate(f5,0, math.pi,i*1000)
	i=i+1
print ("iterations required with integrate",i)


approx=0
i=1
while abs(approx-float(2.0)) > 10e-10:
#for i in range(1,3):
	#print ("here",i,numpy_integrate(f5,0, math.pi,i*1000))
	approx=numpy_integrate(f5,0, math.pi,i*1000)
	i=i+1
print ("iterations required with numpy_integrate",i)

approx=0
i=1
while abs(approx-float(2.0)) > 10e-10:
#for i in range(1,10):
	#print ("here",i,integrate(f5,0, math.pi,i*1000))
	approx=numba_integrate(f5,0, math.pi,i*1000)
	i=i+1
print ("iterations required with numba_integrate",i)

approx=0
i=1
while abs(approx-float(2.0)) > 10e-10:
#for i in range(1,10):
	#print ("here",i,integrate(f5,0, math.pi,i*1000))
	approx=cython_integrate(f5,0, math.pi,i*1000)
	i=i+1
print ("iterations required with cython_integrate",i)


approx=0
i=1
while abs(approx-float(2.0)) > 10e-10:
#for i in range(1,10):
	#print ("here",i,integrate(f5,0, math.pi,i*1000))
	approx=midpoint_integrate(f5,0, math.pi,i*1000)
	i=i+1
print ("iterations required with midpoint_integrate",i)

approx=0
i=1
while abs(approx-float(2.0)) > 10e-10:
#for i in range(1,10):
	#print ("here",i,integrate(f5,0, math.pi,i*1000))
	approx=numpy_midpoint_integrate(f5,0, math.pi,i*1000)
	i=i+1
print ("iterations required with numpy_midpoint_integrate",i)

approx=0
i=1
while abs(approx-float(2.0)) > 10e-10:
#for i in range(1,10):
	#print ("here",i,integrate(f5,0, math.pi,i*1000))
	approx=numba_midpoint_integrate(f5,0, math.pi,i*1000)
	i=i+1
print ("iterations required with numba_midpoint_integrate",i)

approx=0
i=1
while abs(approx-float(2.0)) > 10e-10:
#for i in range(1,10):
	#print ("here",i,integrate(f5,0, math.pi,i*1000))
	approx=cython_midpoint_integrate(f5,0, math.pi,i*1000)
	i=i+1
print ("iterations required with cython_midpoint_integrate",i)



