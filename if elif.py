
'''
temp=30
print(temp <=40 and temp >=20)
print(temp <=25 or temp>=20)
print(not temp <=40)

temp=30
if(temp<=40 and temp>=20):
    print('it is very hot')
    print('take much fluids')
elif (temp <= 35 or temp >= 20):
    print("it is moderate today")
elif (not temp == 20):
    print("temperature cant be predicted")
else:
    ('whatever the temperature is , i have to be there')
'''

# write a weight conversion program in python eg kg in pounds,lbs
weight=float(input('Enter weight'))
unit=input('Enter unit')
if unit.lower()=='kg':
    lbs=weight*2.2
    print('Weight converted into pounds is',lbs)
elif unit.lower()=='lbs':
    kg=weight*0.45
    print('Weight converted into kg is',kg)
else:
    print('Wrong units entered')

