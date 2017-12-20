from polynomials import Polynomial

############################ Test Evaluation of Polynomials
# Define  Test Polynomial
practice=Polynomial([6,5,4,3])

def test_eval_polynomial1():

	#assert practice.__call__(2) ==56
	assert practice(2) == 56

def test_eval_polynomial2():
	assert practice(0) == 6
	#assert practice.__call__(0) ==6

def test_eval_polynomial3():
	assert practice(-2)==-12
	#assert practice.__call__(-2) ==-12

############################ Test Addition of Polynomials
# Define Test Polynomials
p1=Polynomial([6,5,4,3])
p2=Polynomial([-6,1,1,-3])
#print ("ooooooo", type(p2),p2.coefficients)
#print ("here", p2.coefficients)
def test_add_polynomials():
	#assert p1.__add__([-6,1,1,-3])==Polynomial([0,6,5,0])
	#print ("here", p2.coefficients)
	#print ("lol",p2.coefficients,p1.__add__(p2.coefficients))
	#assert p1.__add__(p2.coefficients)==Polynomial([0,6,5,0])
	assert(p1+p2)==Polynomial([0,6,5,0])

############################ Test Subtraction of Polynomials
# Define Test Polynomials
p1=Polynomial([6,5,4,3])
p2=Polynomial([-6,1,1,-3])

def test_subtract_polynomials():
	#assert p1.__sub__([-6,1,1,-3])==Polynomial([-12,-4,-3,-6])
	#print(p2.coefficients,p1.coefficients,"kkk")
	#print((p1-p2))
	#print(p1.__sub__(p2), "righthere")
	#print((p2-p1), "lollllll")

	assert(p2-p1)==Polynomial([-12,-4,-3,-6])

############################ Test Degree Method
# Define Test Polynomials
p4=Polynomial([6,5,4,3])
p5=Polynomial([0,1,1,0])
p3=Polynomial([-3])

def test_degree_polynomials1():

	assert(p4.degree())==3

def test_degree_polynomials2():

	assert(p5.degree())==2

def test_degree_polynomials3():

	assert(p3.degree())==0

####### Define Test Repr. Method

def test_repr_polynomial():
	assert practice.__repr__()==" 3x^3 + 4x^2 + 5x^1 + 6x^0"

####### Define Test Multiplication

def test_mult_polynomial():
	assert (p5*5)==Polynomial([0,5,5,0])

#print(test_eval_polynomial1())
#print(test_eval_polynomial2())
#print(test_eval_polynomial3())
print(test_add_polynomials())
print(test_subtract_polynomials())
print(test_degree_polynomials1())
print(test_degree_polynomials2())
print(test_degree_polynomials3())
print(practice.__repr__())
print(test_repr_polynomial(), ";")
print(test_repr_polynomial())

