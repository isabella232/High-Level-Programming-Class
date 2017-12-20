from time import time
from cython_integrator import cython_integrate

def f3(x):

	return x*x

t0 = time()
cython_integrate(f3,0,1,100000)
t1 = time()
total_time=t1-t0
print("total time",total_time)

