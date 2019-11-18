'''
 This Python program show recusion function(factorial)
 @author R.Gopalakrishnan
 @author gopalakrishnanr94@gmail.com
 @author www.rgopalakrishnanmca.simplesite.com
'''

def factorial(num):
	if num == 1:
		return 1
	else:
		return num * factorial(num -1)


print(factorial(2))
print(factorial(5))	