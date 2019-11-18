'''
 This Python program show string operations
 @author R.Gopalakrishnan
 @author gopalakrishnanr94@gmail.com
 @author www.rgopalakrishnanmca.simplesite.com
'''

# declare string
first_name="JamesBond"
last_name=" OO7"

# cancatenation operation
name=first_name+last_name
print(name)

# access element via index
print(name[2])
print(name[:10])
print(name[10:])
print(name[-1])

# repetition of string
print(name*3)

# membership operator 
print(first_name in name)
print(name in first_name)
print(name not in first_name)

# relational operator
'''
The ASCII value of a is 97, b is 98 and so on.
The ASCII value of A is 65, B is 66 and so on.
'''
str1="abc"
str2="ABC"
str3="aBc"
str4="AbC"

print(str1>str2)
print(str3>str4)
print(str4>str3)