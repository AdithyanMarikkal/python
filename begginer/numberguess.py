import math
import random

lower = int(input("enter the lower bound"))
upper = int(input("enter the upper bound"))
x=random.randint(lower,upper)
totalchances=math.ceil(math.log(upper - lower +1,2))
print("\n\tyou have ",totalchances ,"chances")
count = 0
flag = False
while count < totalchances:
    count+=1
    gues=int(input("\nguess number :-"))
    if gues == x:
        flag=True
        break
    else:
        print(" wrong number!")
    
if flag:
    print("congrats")
else:
    print("\n the number is ",x,"better luck next time")