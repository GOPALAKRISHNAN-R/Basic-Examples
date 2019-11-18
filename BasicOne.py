'''
 This Python program consists of basic data types
 @author R.Gopalakrishnan
 @author gopalakrishnanr94@gmail.com
 @author www.rgopalakrishnanmca.simplesite.com
'''

# int type
num=5									
print(num)								
print(type(num))						

# binary to decimal convertion
_dnum=0b101
print(_dnum)					# Result 5

# octal to decimal convertion
_onum=0o32
print(_onum)					# Result 26

# hexa-decimal to decimal convertion
_hnum=0xf
_hnumm=0xff
print(_hnum)					# Result 15
print(_hnum)					# Result 225

# float type
num=5.6									
print(num)								
print(type(num))						

# complex type
num=5.6j								
print(num)								
print(type(num))						

#isinstance()
n=5
print(isinstance(n,int))
print(isinstance(n,float))
print(isinstance(n,complex))


# string type
string='Python'							
print(string)							
print(type(string))						

# tuple
t1=1,2,3,4,5,6 
t2=('a','b','c','f',1)
print(t1)
print(t2)
print(type(t2))
print(type(t2))

# list
lst1=[1,2,3,4,5]
print(lst1)
print(type(lst1))

# Dictionary(dict)
dic={1:'james',2:'bond','a':'OO7'}
print(dic)
print(dic['a'])
print(dic[2])
print(type(dic))

# set
sett={1,'a','james','bond'}
print(sett)
print(type(sett))