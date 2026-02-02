#Write a Python program to calculate the sum of digits of a number.

num= int(input("Input any number- "))
sum=0

num=abs(num)

while num>0:
       temp= num%10
       sum+=temp
       num=num//10
# sum+=num
print(sum)