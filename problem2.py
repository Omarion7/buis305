import math
from math import pi

radius=float(input('enter radius'))
if(radius>0):
    print('valid input')
    area=3.14*radius*radius
else:
    print('invalid input')
def area():
    radius=float(input("enter radius"))
    area=float(pi)*pow(radius,2)
    print("the area is"+str(area))
