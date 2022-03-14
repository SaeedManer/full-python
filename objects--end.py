#Classes and Objects

'''
class robot:
    def introduce_self(self):
        print("My name is " + self.name)

r1 = robot()
r1.name = "Flash"
r1.color = "red"

r1.introduce_self()
'''
'''
class bike:
    def __init__(imp,n1,c1,m1,con1):
        imp.name = n1
        imp.color = c1

    def att(imp):
        print('My bike name is ' + imp.name + '. It is '+ imp.color + ' in color')

b1 = bike('ducati', 'black', '2022', 'good')
b1.att()


class human:
    def __init__(imp2,n2,c2,t2):
        imp2.name = n2
        imp2.color = c2


    def my(imp2):
        print(imp2.name + ' is a footballer')


h1 = human('Ronaldo', 'white', 'tall')
h1.my()
'''

#Inheritance
#Inheritance
'''
class me:
    def __init__(self, name, surname, name2):
        self.n = name
        self.s = surname
        self.n2 = name2
    def pn(self):
        print ('My name is ' + self.n , self.s)
        print ('My brother name is',self.n2)



m = me('Saeed', 'Maner', 'Lukman')
m.pn()

'''



'''

#parent class

class me:
    def __init__(self, name, surname,):
        self.n = name
        self.s = surname
        
    def pn(self):
        print ('My name is ' + self.n , self.s)


# child
class me2(me):
    def __init__(s1, name, surname,year):
       super().__init__(name, surname)
       s1.y1 = year

    def well(self):
        print('i was born in year', self.y1)


# child2
class me3(me2):
    def __init__(s2, name, surname,year,name2):
        super().__init__(name, surname,year)
        s2.n2 = name2

    def wel(self):
        print('My brother name is',self.n2 )


#Object
a = me3('Saeed', 'Maner', 1999, 'Lukman')
a.wel()

'''

#Iterator
#Iterator
'''
myfruit = ('apple', 'banana', 'cherry')
my = iter(myfruit)

print(next(my))
print(next(my))
print(next(my))
'''

'''
mystr = 'cherry'
my = iter(mystr)

print(next(my))
print(next(my))
print(next(my))
print(next(my))
print(next(my))
print(next(my))
'''

# Scope
# Scope


# global and local scope


'''
y = 500


def func1():
    y = 300
    print(y)

func1()

print(y)
'''
'''
y = 200

def my1():
  global x
  x = 300

my1()

print(x)

'''


# Module
# Module

'''
import mymodule

a = mymodule.person1["age"]
print(a)


import mymodule

mymodule.greeting("Jonathan")

'''


#Dates
#Dates


'''
import datetime

x = datetime.datetime.now()

print(x)


import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
'''


# RegEx Module
# RegEx Module

'''
import re

txt = "the rain in India"
x = re.search('^the.*India$', txt)

if x:
    print('yes')
else:
    print('No')
'''

'''
import re
txt = 'Hello India, Welcome All'

x = re.findall('We.*e',txt)
print(x)
'''

'''
import re
txt = 'Iam from Earth'

x = re.findall('Earth',txt)
print (x)

if (x):
    print('Thereis a match')
else:
    print('No match')


import re
txt = 'Iam from Earth'

x = re.findall('Dune',txt)
print (x)

if (x):
    print('Thereis a match')
else:
    print('No match')
'''

'''
import re
txt = 'I am from Earth'

x = re.split("\s",txt)
print (x)


'''
'''
import re
txt = 'I am from Earth'


x = re.search("\s",txt)

print("The first gf hg:", x.start())


'''

'''
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start()) 

'''


#Try... Except
#Try... Except

'''
try:
  print(x)
except:
  print("An exception occurred")
'''

'''
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
'''



username = input("Enter username:")
print("Username is: " + username)





































    
