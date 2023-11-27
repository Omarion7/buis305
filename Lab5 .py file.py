number1=int(input('enter number1:'))
if(number1%3==0 and number1%5==0):
    print('Tic Tac')
elif(number1%5==0):
    print('Tac')
elif (number1%3==0):
    print('Tic')
else:
    print(number1)

count=0
while(count<21):
    print(count)
    count=count+1




