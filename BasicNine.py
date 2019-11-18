'''
 This Python program show list operations
 @author R.Gopalakrishnan
 @author gopalakrishnanr94@gmail.com
 @author www.rgopalakrishnanmca.simplesite.com
'''

# declare list values
lst=[1,2,3,4,5,6,77]

# access values via index
print(lst[2])
print(lst[:])

for x in lst:
	print(x)

# insert operation
lst.insert(6,100)					# add value 100 at index position 6
print(lst)

lst.append(22)						# add value 22 at end of the list
print(lst)

lst.extend([99,88,77])				# add multiple element at end of list
print(lst)

# update operation
lst[0]=1000
print(lst)

lst[1:3]=[22,77]				
print(lst)

# delete operation
lst.remove(1000)					# element value to delete
print(lst)

lst.pop(2)							# element index value to delete
print(lst)