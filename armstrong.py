#Write a Python program to check if a given number is an Armstrong number.

num= int(input("Input any number~ "))
org_num=num
digits= []
mod=0
count=0
sum=0

#Counting digits and adding each digits to a list
while(num//10!=0):
       mod=num%10
       digits.append(mod)
       count+=1
       num=num//10
count+=1
digits.append(num)

#Summing each digits
for i in digits:
       sum+=i**count

#Checking conditions for Armstrong
if sum==org_num:
       print(f"{org_num} is an armstrong number.")
else:
       print(f"{org_num} is not an armstrong number.")



