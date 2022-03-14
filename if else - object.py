

# if statement
# if statement

'''
a = 30
b = 100
if b>a:
    print("Yes")
'''


#elif
'''
a = 30
b = 30
if b > a:
    print('yes')
elif a==b:
    print('Right')
'''

#else
'''
a = 300
b = 30
if b > a:
    print('yes')
elif a==b:
    print('Right')
else :
    print('yep..')

'''


#Short hand if
'''
a = 300
b = 100
if a > b: print('a is greater then b')



a = 333
b = 333
print('A') if a>b else print('=') if a == b else print('B')

'''

# IF and AND
'''
a = 30
b = 25
c = 50
if a>b and c>a:
    print('both condition are true')
'''

#pass statement
'''
a =300
b= 400

if b>a:
    pass
'''



# While Loop
# While Loop


'''
a = 2
while a<20:
    print(a)
    a +=2
'''

#break statement

'''
a = 2
while a<20:
    print(a)
    a +=1
    if a == 3:
        break
    a += 1
'''

# The Continue Statement
'''
a = 1
while a < 10:
    print(a)
    a += 1
    if a == 3:
        continue
    print(a)
'''





#python for loop
#python for loop


'''
num = ['1','2','3','4','5','6']
for x in num:
    print(x)

    
for x in 'saeed':
    print(x)
'''

'''
num = ['1','2','3','4','5','6']
for x in num:
    print(x)
    if x == '4':
        break
   ''' 
'''
num = ['1','2','3','4','5','6']
for x in num:
    if x == '4':
        continue
    print(x)

'''

'''
for x in range (10):
    print(x)
'''

'''
for x in range (2,10,2):
    print(x)
'''
'''
for x in range (10):
    print(x)
else:
    print('finish')
'''
'''
for x in range (10):
    if x == 4: break
    print(x)
else:
    print('finish')
'''

'''
fruit = ['apple', 'banana', ]
color = ['red', 'yellow', ]
for x in fruit:
    for y in color:
        print(x,y)
'''

# While Loops
# While Loops

'''
a = 1
while a < 20:
    print (a)
    a +=2
'''
'''
a = 2
while a < 20:
    print (a)
    a +=2
'''


# Break Statement
'''
a = 2
while a < 20:
    print (a)
    if a == 10:
        break
    a +=1


a = 51
while a < 60:
    print (a)
    if a == 55:
        break
    a +=1
'''

# Continue Statement
'''
a = 51
while a < 60:
    a +=1
    if a == 55:
        continue
    print(a)
'''

# else statement

'''
a = 51
while a < 60:
    print(a)
    a +=1
else:
    print("a is not greater than 60")
''' 




#Python Function
#Python Function

'''
def my_function():
    print("Saeed")

my_function()


def my_function(x):
    print(x + "Saeed")

my_function("name")
my_function("contc")
my_function("phone")
'''

'''
def my_function(name, surname):
    print(name + ' ' + surname)

my_function("saeed", "maner")
'''

'''
def my(x1,x2,x3):
    print("my name is " + x2)
my('uaise','lukman','saeed',)


def my(**x):
    print("my name is " + x(1))
my('uaise','lukman','saeed',)

'''

'''
def m1(name = "Saddam"):
    print("My name is " + name)

m1("Saeed")
m1("Lukman")
m1("Uaise")
m1("Sohail")
'''



#Arrays
#Arrays

'''
car = ['BMW','mercedes','ferari']

x = car[0]

print(x)


car = ['BMW','mercedes','ferari']

car[1] = 'toyota'

print(car)
'''


#length of an array

'''

car = ['BMW','mercedes','ferari']

print(len(car))
'''

#looping Array 

'''
cars = ['BMW','mercedes','ferari']
for a in cars:
    print(a)

'''

# Adding Array Element

'''
cars = ['BMW','mercedes','ferari']

cars.append('Honda')

print(cars)

'''

#removing array element

'''

student = ['name', 'email', 'contact no.']
student.pop(2)
print(student)


student = ['name', 'email', 'contact no.']
student.remove('email')
print(student)

'''


# Class and Objects
# Class and Objects

'''

class new:
    x = 1
    y = 2 
    z = 3
a1 = new()
print(a1.x)
print(a1.y)

'''
































