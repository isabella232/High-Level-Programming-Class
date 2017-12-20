from time import time
# perform numerical integration

cpdef double cython_integrate(f,double a,double b,int N):

	cdef double diff=b-a
	cdef double inc=float(diff)/float(N)
	cdef double sum=0
	cdef double x=0
	cdef int i
	cdef double val
	cdef double lower
	cdef double area

	for i in range(N):

		val=a+(i*inc)
		x=val
		#print(x)
		lower=f(val)
		#print ("l",lower)

		area=(lower*(inc))
		#print ("a",area)

		sum+=area

	return sum

cpdef double cython_midpoint_integrate(f,double a,double b,int N):

	cdef double diff=b-a
	cdef double inc=float(diff)/float(N)
	cdef double sum=0
	cdef double x=0
	cdef int i
	cdef double val
	cdef double lower
	cdef double val2
	cdef double upper
	cdef double mid
	cdef double area

	for i in range(N-1):

		val=a+(i*inc)
		x=val
		val2=a+((i+1)*inc)
		#print(x)
		lower=f(val)
		upper=f(val2)
		mid=(lower+upper)/float(2.0)
		#print ("l",lower)

		area=(mid*(inc))
		#print ("a",area)

		sum+=area

	return sum


