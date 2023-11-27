#number1= int(input('Enter number1 :'))
#tmpcount=0
#while(number1<=0 and tmpcount<4):
   # print(number1)
   # number1= float(input('Enter number1 greater than 0:'))
  #  print(tmpcount,"tmpcount")
  #  tmpcount=tmpcount+1
#print('you are smart')

import random


#name='Alan Turing'
#print(name[0])

#data='I am in Buis305-001. Test123'
#for i in data:
    #print(i)

#for i in range (len(data)):
   # print(i,data[i])

#test='I like food!'
#for i in test:
   # print(i)
#for i in range(len(test)):
    #print(i,test[i])

#data='myfile.txt'
#print(data[0:3])
#print(data[1:3])

#filelist=['myfile.txt','myprogram.exe','yourfile.txt']
#for i in filelist:
   # if '.txt' in i:
   #     print(i)
#for m in filelist:
  #  if'.exe' in m:
    #    print(m)

#f=open("myfile.txt",'w')
#f.write("first line. \nSecond line1.\n")
#f.close()
#print('I am done!')

import random
f=open('integers.txt', 'w')
for count in range (500):
    number=random.randint(1,500)
    f.write(str(number) + '\n')
f.close()
