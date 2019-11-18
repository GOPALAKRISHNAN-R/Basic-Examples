'''
 This Python program show class and object 
 @author R.Gopalakrishnan
 @author gopalakrishnanr94@gmail.com
 @author www.rgopalakrishnanmca.simplesite.com
'''

class Test:
	"""This document contains class and object example..!!!"""

	# instance attribute
	str1="welcome to Python!!"


	# instance behaviour
	def sayHello(self):
		print("Hi! folks...")

# creating object for a class
obj=Test()

# accessing element
# print(__doc__)				
print(obj.__doc__)
print(obj.str1)
obj.sayHello()		