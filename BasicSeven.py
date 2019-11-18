'''
 This Python program show function basics
 @author R.Gopalakrishnan
 @author gopalakrishnanr94@gmail.com
 @author www.rgopalakrishnanmca.simplesite.com
'''


# function without parameter and without return
def say_hello():
	print("Welcome to Python!!")


# function with parameter and without return
def add_two(a,b):
	print(a+b)
	

# function with parameter and with return
def fun_sub(c,d):
	return(c-d)
	

# function with default value
def fun_mul(a=5,b=2):
	return a*b
	

# calling functions
say_hello()

add_two(5,7)

sub=fun_sub(10,5)
print(sub)

print(fun_mul(9))

print(fun_mul(10,10))	