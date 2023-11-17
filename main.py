#Identation
if 5 > 2:
    print("Five is greater than two")

#variables
userage = 30
username= "George"
print(userage)
print(username)

#typesofvariables
myVariableName="camel case George"
MyVariableName="pascal case George"
my_variable_name="snake case George"
print(myVariableName)
print(MyVariableName)
print(my_variable_name)

#printfunction
x= "you know,nothing, jon snow"
print(x)
a = "Jon Snow"
b = "is"
c = "cool"
print (a,b,c)

#datatypes
digit1= 100
print(digit1)
print(type(digit1))
digit2 = 1.25
print(digit2)
print(type(digit2))
digit3=2j
print(digit3)
print(type(digit3))

#randomlibrary
import random
print(random.randrange(1,100))

#casting
y= int(1)
z= int(1.5)
t= int("1")
print(type(y))
print(type(z))
print(type(t))

b = float(1)
c = float(2.0)
d= float("3")
e = float("4.0")
print(type(b))
print(type(c))
print(type(d))
print(type(e))
#string
f = str(1)
g = str(1.0)
print(type(f))
print(type(g))

#strings
string1 = "will not, or cannot?"
print(string1)
print(type(string1))
string2 = "to hell with your clan, NO, TO HELL WITH YOU!!"
string3 = string1 + string2
print(string3)

#python booleans
digit4 = 10
digit5 = 50
if digit5 > digit4:
    print("digit 5 is more than digit 4")
else:
    print("digit 4 is less than digit 5")

#arithmetic operators
#sum
h = 30
i = 30
j = h+i
print(j)
#subtraction
k = i-h
print(k)
#multiplication
l = h*i
print(l)
#division
m=i/h
print(m)
#modulus
n= i%h
print(n)

#list
thislist = ["apple","banana","cherry","mango"]
print(thislist)
#accesslists
print(thislist[0])
#negativeindexing
print(thislist[-1])
#rangeofindexes
print(thislist[1:4])

#whileloop
o = 1
while o < 6:
    print (o)
    o+=1

 #breakstatement
p = 1
while p <6:
    print(p)
    if p==3:
        break
    p+=1

#else statement
q = 1
while q <6:
    print(q)
    q+=1
else:
    print("q is more than 1")

#forloops
cars = ["toyota","subaru","volkswagon","ferrari","nissan"]
for x in cars:
    print(x)

#functions
def myfunction():
    print("this is a function")
myfunction()

#input
name = input("what is your name:")
print("your name is:" +name )