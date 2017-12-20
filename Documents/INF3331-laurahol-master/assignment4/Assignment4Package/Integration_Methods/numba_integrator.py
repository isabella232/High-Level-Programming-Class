#from matplotlib import pyplot
import numpy as np
from time import time
from numba import jit
# perform numerical integration

def f2(x):
	return 2*x

def f1(x):
	return 2

def f3(x):

	return x*x

@jit
def numba_integrate(f,a,b,N):

	a=float(a)
	b=float(b)
	diff=b-a
	inc=float(diff)/float(N)
	sum=0
	x=0
	NParray=np.arange(0,N)
	#print (NParray)
	x_vals=a+(NParray*inc)
	#print (x_vals)
	lower=f(x_vals)
	if type(lower)==int:
		lowerint=lower
		lower=np.empty(N)
		lower.fill(lowerint)
	#print("l",type(lower),lower)
	area=lower*(inc)
	#print(area)
	sum=np.sum(area)
	return sum

@jit
def numba_midpoint_integrate(f,a,b,N):

	a=float(a)
	b=float(b)
	diff=b-a
	inc=float(diff)/float(N)
	sum=0
	x=0
	NParray1=np.arange(0,N-1)
	NParray2=np.arange(1,N)
	#print (NParray)
	x_vals1=a+(NParray1*inc)
	x_vals2=a+(NParray2*inc)
	#print (x_vals1)
	lower=f(x_vals1)
	upper=f(x_vals2)
	if type(lower)==int:
		lowerint=lower
		lower=np.empty(N)
		lower.fill(lowerint)
	if type(upper)==int:
		upperint=upper
		upper=np.empty(N)
		upper.fill(upperint)
	#print("l",type(lower),lower)
	mid=(lower+upper)/float(2.0)
	area=mid*(inc)
	#print(area)
	sum=np.sum(area)
	return sum

x_vals=[]
y_vals=[]

#for j in range(1,101):
#	x_vals.append(j*20)
#	y_vals.append(abs((float(1)/float(3))-numpy_integrate(f3,0,1,j*20)))

#	#print (j*20,abs(((float(1)/float(3))-numpy_integrate(f3,0,1,j*20))))

##print(numba_integrate(f1,0,1,10))
##print(numba_integrate(f2,0,1,10))
#t0 = time()
#numba_integrate(f3,0,1,100000)
#t1 = time()
#total_time=t1-t0
##print(total_time)


#plt.plot(x_vals,y_vals)
#plt.xlabel('N')
#plt.ylabel('error')
#plt.show()
#plt.savefig('quadratic_error.png')


