'''
 This Python program shows looping statements(while,for)
 @author R.Gopalakrishnan
 @author gopalakrishnanr94@gmail.com
 @author www.rgopalakrishnanmca.simplesite.com
'''

# while loop
_i=20
while _i>0:
	print(_i)
	_i-=1

# for loop
t1=(1,2,3,4,5,6)
print(t1)						# prints single line
for x in t1:
	print(x)

# print 0 to 5
for i in range(6):
	print(i)

# print sum of 5 natural numbers
sum=0
for i in range(5):
	sum=sum+i
print(sum)

# nested loops
for inner in range(3): 							# outter loop prints 0,1,2
	for outter in range(3): 					# inner loop prints 0,1,2
	# 	print("inner loop execute:",j)
	# print("outter loop execute:",i)
		print(inner,outter)