number1=int(input('enter number1:'))
if(number1%3==0 and number1%5==0):
    print('Tic Tac')
elif(number1%5==0):
    print('Tac')
elif (number1%3==0):
    print('Tic')
else:
    print(number1)

count=1
while(count<21):
    print(count,end=',')
    if(count % 3==0 and count % 5==0):
        print('TicTac ')
    elif(count % 5 ==0):
        print('Tac')
    elif(count % 3==0):
        print('Tic')
    count=count+1

import random
print(random.randint(50,100))

attempts=1
user_value=0

while attempts <5 and user_value<=0:
    user_value=int(input('Enter a positive number'))
    if user_value<=0:
        print('value must be greater than 0. Try again.')

    if random==user_value:
        print('perfect match!')
    else:
        print()





