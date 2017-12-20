#from matplotlib import pyplot
import numpy
from time import time
# perform numerical integration

#def f1(x):
#	return 2*x

def f1(x):
	return 2

def f3(x):

	return x*x

def integrate(f,a,b,N):
	a=float(a)
	b=float(b)
	diff=b-a
	inc=float(diff)/float(N)
	sum=0
	x=0

	for i in range(0, N):

		val=a+(i*inc)
		x=val
		#print(x)
		lower=f(val)
		#print ("l",lower)

		area=(lower*(inc))
		#print ("a",area)

		sum=sum+area

	return sum

def midpoint_integrate(f,a,b,N):
	a=float(a)
	b=float(b)
	diff=b-a
	inc=float(diff)/float(N)
	sum=0
	x=0

	for i in range(0, N-1):

		val=a+(i*inc)
		x=val
		xplusone=a+((i+1)*inc)
		#print(x)
		lower=f(val)
		upper=f(xplusone)
		mid=float(lower+upper)/float(2.0)
		#print ("l",lower)

		area=(mid*(inc))
		#print ("a",area)

		sum=sum+area

	return sum

x_vals=[]
y_vals=[]

for j in range(1,101):
	x_vals.append(j*20)
	y_vals.append(abs((float(1)/float(3))-integrate(f3,0,1,j*20)))

	#print (j*20,abs(((float(1)/float(3))-integrate(f3,0,1,j*20))))


#plt.plot(x_vals,y_vals)
#plt.xlabel('N')
#plt.ylabel('error')
#plt.show()
#plt.savefig('quadratic_error.png')

t0 = time()
integrate(f3,0,1,100000)
t1 = time()
total_time=t1-t0
#print(total_time)


