'''
 This Python program show dictionary operations
 @author R.Gopalakrishnan
 @author gopalakrishnanr94@gmail.com
 @author www.rgopalakrishnanmca.simplesite.com
'''

# declaration
dic={"st_name":"James","clg":"au","age":25}

# accessing
print("Single line display:",dic)
print("Display student name:",dic["st_name"])
print("Display student name and college:",dic["st_name"],dic["clg"])

for e in dic:
	print("key:",e ,"values:",dic[e])
	
# deletion
del dic