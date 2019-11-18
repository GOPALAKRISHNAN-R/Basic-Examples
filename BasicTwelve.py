'''
 This Python program show class and object 
 @author R.Gopalakrishnan
 @author gopalakrishnanr94@gmail.com
 @author www.rgopalakrishnanmca.simplesite.com
'''

class College:
	# instance attributes
	def __init__(self,regno,name,clss):
		self.regno=regno
		self.name=name
		self.clss=clss

	# behaviour
	def studying(self,books):
		return "{} is studing {}".format(self.name, books)

# creating object for College class
gopal=College(1,"Gopalakrishnan","MCA")
arun=College(2,"ArunKumar","B.com")

# accessing object from information
print(gopal.studying("Python"))
print(arun.regno,arun.name,arun.clss)