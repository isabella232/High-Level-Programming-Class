from Assignment4Package.Integration_Methods.integrator import integrate
from Assignment4Package.Integration_Methods.numpy_integrator import numpy_integrate
from Assignment4Package.Integration_Methods.cython_integrator import cython_integrate


# Define Test Function

def f1(x):
	return 2

def f2(x):
	return 2*x

############################ Test Evaluation of Polynomials
# Define Integrator Tests

def test_integral_of_constant_function():

# test integrate

	assert abs(integrate(f1,0,1,1)-2)<= 1E-15
	#print ("lol",abs(integrate(f1,0,1,10000)-float(2)))
	assert abs(integrate(f1,0,1,10)-2)<= 1E-12
	assert abs(integrate(f1,0,1,100)-2)<= 1E-12
	assert abs(integrate(f1,0,1,1000)-2)<= 1E-12
	assert abs(integrate(f1,0,1,10000)-2)<= 1E-12

# test numpy integrate

	assert abs(numpy_integrate(f1,0,1,1)-2)<= 1E-15
	#print ("lol",numpy_integrate(f1,0,1,10),abs(numpy_integrate(f1,0,1,10)-float(2)))
	assert abs(numpy_integrate(f1,0,1,10)-2)<= 1E-12
	assert abs(numpy_integrate(f1,0,1,100)-2)<= 1E-12
	assert abs(numpy_integrate(f1,0,1,1000)-2)<= 1E-12
	assert abs(numpy_integrate(f1,0,1,10000)-2)<= 1E-12

# test Cython

	assert abs(cython_integrate(f1,0,1,1)-2)<= 1E-15
	#print ("lol",numpy_integrate(f1,0,1,10),abs(numpy_integrate(f1,0,1,10)-float(2)))
	assert abs(cython_integrate(f1,0,1,10)-2)<= 1E-12
	assert abs(cython_integrate(f1,0,1,100)-2)<= 1E-12
	assert abs(cython_integrate(f1,0,1,1000)-2)<= 1E-12
	assert abs(cython_integrate(f1,0,1,10000)-2)<= 1E-12

def test_integral_of_linear_function():

# test integrate

	N1=10
	#print ("here",abs(1-integrate(f2,0,1,N1)-(float(1)/float(N1))))
	assert abs(1-integrate(f2,0,1,N1)-(float(1)/float(N1))) <= 1E-15

	N2=100

	assert abs(1-integrate(f2,0,1,N2)-(float(1)/float(N2))) <= 1E-15

	N3=1000

	assert abs(1-integrate(f2,0,1,N3)-(float(1)/float(N3))) <= 1E-15

	N4=10000

	assert abs(1-integrate(f2,0,1,N4)-(float(1)/float(N4))) <= 1E-15

# test numpy integrate

	N1=10

	assert abs(1-numpy_integrate(f2,0,1,N1)-(float(1)/float(N1))) <= 1E-15

	N2=100

	assert abs(1-numpy_integrate(f2,0,1,N2)-(float(1)/float(N2))) <= 1E-15

	N3=1000

	assert abs(1-numpy_integrate(f2,0,1,N3)-(float(1)/float(N3))) <= 1E-15

	N4=10000

	assert abs(1-numpy_integrate(f2,0,1,N4)-(float(1)/float(N4))) <= 1E-15

# test Cython

	N1=10

	assert abs(1-cython_integrate(f2,0,1,N1)-(float(1)/float(N1))) <= 1E-15

	N2=100

	assert abs(1-cython_integrate(f2,0,1,N2)-(float(1)/float(N2))) <= 1E-15

	N3=1000

	assert abs(1-cython_integrate(f2,0,1,N3)-(float(1)/float(N3))) <= 1E-15

	N4=10000

	assert abs(1-cython_integrate(f2,0,1,N4)-(float(1)/float(N4))) <= 1E-15


######################
print(test_integral_of_constant_function())
print(test_integral_of_linear_function())

