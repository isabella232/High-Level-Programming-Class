# do we want to change the initaly polynomial with each operation permanently?
class Polynomial:

	def __init__(self, coefficients):
		"""coefficients should be a list of numbers with 
		the i-th element being the coefficient a_i."""
		self.coefficients = coefficients

	def degree(self):
		"""Return the index of the highest nonzero coefficient.
		If there is no nonzero coefficient, return -1."""
		# find last entry of coefficients list
		l=len(self.coefficients)-1

		highest_zero=-100
		highest_degree=len(self.coefficients)-1

		for i in range(0, len(self.coefficients)):

			if self.coefficients[i]==0:
				#print (i)
				highest_zero=i

		if highest_zero==(len(self.coefficients))-1:
			#print ("YesY")
			for i in range(0, len(self.coefficients)):
				if self.coefficients[l-i]!=0:
					#print ("Plo", self.coefficients[l-i])
					#print (i)
					highest_degree=l-i
					break;

		if all([ v == 0 for v in self.coefficients]):
			highest_degree=-1

		return highest_degree

	def coefficients(self):
		"""Return the list of coefficients. 

		The i-th element of the list should be a_i, meaning that the last 
		element of the list is the coefficient of the highest degree term."""
		#self.coefficients = coefficients

	def __call__(self, x):
		"""Return the value of the polynomial evaluated at the number x"""
		counter=0
		sum=0
		for i in range(0, len(self.coefficients)):
			#print(i)
			sum=sum+(self.coefficients[i]*(x**counter))
			#print ("sum",sum)
			counter=counter+1
		return sum

############

	def __add__(self, p):
		"""Return the polynomial which is the sum of p and this polynomial
		Should assume p is Polynomial([p]) if p is int. 
		# put 0's in place where there is a coefficient  in one polynomial but not in the other
		If p is not an int or Polynomial, should raise ArithmeticError."""

		if type(p) is not int and type(p) is not Polynomial:
			#print (type(p), "type p")
			raise ArithmeticError

		a=list(self.coefficients)
		if type(p) is list:
			b=list(p)
		if type(p) is int:
			temp=[]
			temp.append(p)
			b=temp
		if type(p) is Polynomial:
			#print (p.coefficients)
			#print ("Test8",p,p.coefficients)
			#print(p.coefficients)
			b=list(p.coefficients)



		max_list_length = max(len(a),len(b))
		if len(a) >= len(b):
			c=a
			d=b
		else:
			c=b
			d=a
		for i in range(0, len(d)):
			c[i]=c[i]+d[i]

		return c

	def __sub__(self, p):
		"""Return the polynomial which is the difference of p and this polynomial
		Should assume p is Polynomial([p]) if p is int. 

		If p is not an int or Polynomial, should raise ArithmeticError."""

		if type(p) is not int and type(p) is not Polynomial:

			raise ArithmeticError

		b=list(self.coefficients)
		if type(p) is list:
			a=list(p)
		if type(p) is int:
			temp=[]
			temp.append(p)
			a=temp

		if type(p) is Polynomial:
			#print (p.coefficients)
			#print ("Test8",p,p.coefficients)
			#print(p.coefficients)
			a=list(p.coefficients)

		max_list_length = max(len(a),len(b))

		if len(a) >= len(b):

			diff=len(a)-len(b)

			for i in range(0,diff):
				b.append(0)

			c=b
			d=a
			for i in range(0, len(d)):
				#print (c[i],d[i], "here")
				c[i]=c[i]-d[i]
		else:
			c=b
			d=a
			for i in range(0, len(d)):
				c[i]=c[i]-d[i]

		return c

	def __mul__(self, c):
		"""Return the polynomial which is this polynomial multiplied by given integer.
		Should raise ArithmeticError if c is not an int."""

		if type(c) is not int:
			raise ArithmeticError

		e=list(self.coefficients)
		for i in range(0, len(e)):
			e[i]=e[i]*c
		return e

	def __rmul__(self, c):
		"""Return the polynomial which is this polynomial multiplied by some integer"""
		e=list(self.coefficients)
		for i in range(0, len(e)):
			e[i]=e[i]*c
		return e

####################

	def __repr__(self):
		"""Return a nice string representation of polynomial.

		E.g.: x^6 - 5x^3 + 2x^2 + x - 1
		"""
		first=0
		string_to_print=" "
		for i in range(0, len(self.coefficients)):
			var=(len(self.coefficients))-i-1
			#print(var,i)
			if self.coefficients[var]<0:
				self.coefficients[var]=self.coefficients[var]*(-1)
				add_or_subtract=' - '
			else:
				add_or_subtract=' + '
				if i==0:
					add_or_subtract=''

			if self.coefficients[var]!=0:

				if first!=0:

					string_to_print=string_to_print+add_or_subtract+str(self.coefficients[var])+str("x")+'^'+str(var)

				if first==0 and add_or_subtract==' - ':
					string_to_print=string_to_print+add_or_subtract+str(self.coefficients[var])+str("x")+'^'+str(var)
					first=1
				if first==0 and add_or_subtract!=' - ':
					string_to_print=string_to_print+str(self.coefficients[var])+str("x")+'^'+str(var)
					first=1


		return string_to_print


	def __eq__(self, p):
		"""Check if two polynomials have the same coefficients."""

		# remove all 0 coefficients

		Poly1=[]
		Poly2=[]

# Remove all O coefficients

		for i in range(0, len(self.coefficients)):
			if self.coefficients[i]!=0:
				Poly1.append(self.coefficients[i])

		for i in range(0, len(p)):
			if p[i]!=0:
				Poly2.append(p[i])


		if Poly1==Poly2:
			return True
		else:
			return False

############

practice=Polynomial([1,2,3,4,5,0,0,0])

print (practice.degree())
print (practice.coefficients)
print (practice.__call__(2))
print (practice.__add__(2))
print (practice.__sub__(2))
print ("here", practice(2))
print ("mul",practice.__mul__(5))
print ("rep",practice.__repr__())
print ("rep",practice.__eq__([1,2,3,4,5,0,0,0]))



