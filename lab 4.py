import math

for i in range(0,11):
 print(i)
for i in range(1,11):
    print(i)
for i in range(1,11,2):
    print(i)
radius=float(input('enter radius'))
area=math.pi*radius*radius
print(area)
length=float(input('enter length'))
print(length)
breadth=float(input('enter breadth'))
print(breadth)
area=length*breadth
print(area)
radius=float(input('enter radius'))
if(radius>0):
    print('valid input')
    area=3.14*radius*radius
    print(area)
else:
    print('invalid input')






