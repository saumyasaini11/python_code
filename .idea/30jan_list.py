list=['a','bc',70,1.23]
list2=['d',70]
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(list*2)
print(list+list2)

name=['saumya','shivanya','dev','rahul','alia']
print(name[0])
print(name[-4])
name[2]='alia'
print(name[0:3])
name.append('ajay')
print(name)
name.insert(0,'Shree Ram')
print(name)

num_list=[1,2,3,4,5,6,7]
for i in num_list:
    print(i)

i=1
while i<=len(num_list):
    print(i)
    i+=1