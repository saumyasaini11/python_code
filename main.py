# wap to create your biodataand use the input fcx
'''
name=input("Enter your name ")
sap=int(input("Enter sap id "))
address=input('Enter address ')
cllg=int(input("enter cllg year "))
yr=int(input("enter your semester "))
pin=int(input("enter pincode "))
email=input("enter cllg email id ")
'''
# wap to carry various operations on a string there should be atleast 20 operations
'''
a="Hello there!"
b='how are you'
print(a+b)
print(a*3)
print(a.lower())
print(b.upper())
print(b.capitalize())
print(a.count("l"))
print(b.find('o'))
print(id(a))
print(len(b))
print(a.swapcase())
print(b.title())
print(a.index('o'))
print(b.replace('o','x'))
print(a.partition('e'))
print(a.isalnum())
'''

'''
a=float(input('enter the first variable'))
b=input('enter the second variable')
c=a+b
d=a-b
e=a*b
f=a%b
g=a/b
h=a//b
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
'''
# wap to make a calculater that does all arthematic, comparasion and logical operations
a = int(input('enter the first variable'))
b = int(input('enter the second variable'))

print('arthematic operations')
c = a + b
d = a - b
e = a * b
f = a % b
g = a / b
h = a // b
i = a ** b

print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)

print("comparsion operations")
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)
print(a)

print(" bitwise operations ")

print(a & b)
print(a | b)
print(a ^ b)
print(a << 2)
print(b >> 2)

print("logical operations ")
x = True
y = False
print(x and y)
print(x or y)
print(not x)
print(not y)

####
a += b
print(a)
a -= b
print(a)
a %= b
print(a)
