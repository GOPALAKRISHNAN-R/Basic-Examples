'''
 This Python program shows other conditional statements (break,continue,pass)
 @author R.Gopalakrishnan
 @author gopalakrishnanr94@gmail.com
 @author www.rgopalakrishnanmca.simplesite.com
'''

# break statement
numbers=(2,66,88,11,22)
for num in numbers:
	print(num)
	if num == 88:
		print(num,"is found")
		print("Terminating loop")
		break

# continue statement
_numbers=(1,2,3,4,5,6,7,8,11,22)
for _num in _numbers:
	if _num % 2 == 0:
		continue
	print(_num)

# pass statement
given_num=25
if given_num % 2 == 0:
	pass								# tells python interpreter to do nothing
else:
	print(given_num)

	# we use 'pass' statement for future purpose definition for class,method
	# mainly it avoids 
		# SyntaxError in class and 
		# IndentationError in method declaration 
class test:pass

def function():
	pass