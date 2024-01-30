# use of while loop
i = 0;
while i <= 10:
    print(i)
    i += 1

# use of for loop
for i in 'saumya':
    print(i)

# use of range keyword
for i in range(2, 20):
    print(i)

# a series of even number
for i in range(2, 20, 2):
    print(i)

for i in ['welcome', 'to', 'python']:
    print(i)

i = 0
while i <= 10:
    print(i * '*')
    i += 1
##############

a = [1, 2]
b = [3, 4]
for i in a:
    for j in b:
        print('inside the inner loop')
        print(i, j)
    print('outside the inner loop')
##############
sec_num = 7
guess_count = 3
while guess_count <= 3:
    guess = int(input("enter the no. to guess"))
    if guess != sec_num:
        print('try again')
        guess_count += 1
    else:
        guess == sec_num
        print('you won')
        break

# wap to find factorial of a number
num = int(input("enter a number"))
factorial = 1
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)

