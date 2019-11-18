'''
 This Python program shows conditional statements (if,if..else,if elif..else,nested if..else)
 @author R.Gopalakrishnan
 @author gopalakrishnanr94@gmail.com
 @author www.rgopalakrishnanmca.simplesite.com
'''

# if statement
num=100
if num>10:
	print(num,"is greater than 10")

#if else statement
_num=11
if _num % 2 == 0: 
	print("Even Number")
else:
	print("Odd Number")

# if elif else statement
num_=100
if num_<10:
	print("single digit number")
elif num_<100:
	print("Two digit number")
elif num_<1000:
	print("Three digit number")
else:
	print("Four digit number")


# nested if..else statement
num1=-99
if num1>0:
	print("Positive number")
	if num1<10:
		print("single digit number")
	elif num1<100:
		print("Two digit number")
	elif num1<1000:
		print("Three digit number")
	else:
		print("Four digit number")
else:
	print("Negative number")