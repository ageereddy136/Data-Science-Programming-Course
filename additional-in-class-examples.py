# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


print("Hello World")
x = input('Enter something ')
print(x +'5')
print(int(x))
print(type(x))

a=1000
print(id(a))
a=a+1
print(id(a))
b="test"
print(id(b))



x = "myfile.xl"
if x.endswith("xls"):
    print("excel file")
else:
    print(x)



x = "matt"
if (x == "matt"):
    print("Hi Matt")
if (x != "joe"):
    print("Hi Matt")
y=93
if 90 < y <= 100:
     print("You get an A")
     
     
     
x = [14, 3, 8, 2]
y = ['ringo', 'paul', 'john']
x.append(16)
y.append('george')
for i in range(len(x)):
    print(x[i])
for i in y:
    print(i)


names = ["matt", "Matt", "rish","Rish"]
names.sort()

nums=range(5)
print("type of range ", type(nums))
nums=list(nums)
nums.sort()
# defining newlist as a range, converting it to a list and then iterating is similar to working with arrays
# or defining it as a blank list, and then using append to add items to the array
# unlike arrays, the placeholders are pointers

newlist=list()
for i in range(5):
    newlist.append(3)
    newlist.insert(0,4)
print(newlist)

#in-place and copied sorting is important to understand
#create a new list 
sorted_newlist=sorted(newlist)
print(newlist)
print(sorted_newlist)
#in-place-sorting
newlist.sort()
print(newlist)

#creating a list of tuples
#type commands down show that it is a list of tuples
print(type(newlist))
x=list()
for i in range(3):
    x.append(("Matt", i, " Lombard"))
print(x)
print(type(x))
print(type(x[0]))


#dictionaries are unique name-value pairs but can be created in many ways
info = {'first':'blah','last':'blew'}
print(info['first'])
#another way to create a dictionary
info2=dict()
info2['first']='bbb'
info2['age']=20
print(info2)
#iterate over a dictionary
for name in info2:
    print(name,info2[name])
# creating a dict with name-value pairs is easy, then iterating over it is easy as well

#two lists of names. One should be beatles, second should be doors. Then map each name to the list of bands through a dictionary
beatlesnames = ['paul','george']
doorsnames = ['joe','george']
namesbands = {}
for name in beatlesnames:
    if name not in namesbands:
        namesbands[name]=[]
    namesbands[name].append("Beatles")
for name in doorsnames:
    if name not in namesbands:
        namesbands[name]=[]
    namesbands[name].append("Doors")
print(namesbands)

x1=50
import random
def abc(x):
    return x*random.random()
print(abc(5.1))


fp=open('simple.csv')
#iterating through all lines in a text file
#try to print x itself and see the extra newline character
for x in fp:
    print(x[:-1])


class Chair:
    max_occupants=4
    
    def __init__(self, id):
        self.id = id
        self.count=0
    def load(self, number):
        self.count += number
    def unload(self, number):
        self.count -= number

x = Chair(20)
x.load(2)
print(x.count)
        
        
        
        
    