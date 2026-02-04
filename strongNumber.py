#Write a program to check whether a given number is a strong number or not.

#Hint: A Strong Number is a number in which the sum of the factorials of its digits equals the number itself.

print("Strong Number Checker")
num= int(input("The number is .. "))
org_num=num
total=0

if num<0:
       print("Enter valid value (Only positive number.)")

#Function to calcuate the factorial
def factorial(n):
       if n==0 or n==1:
              return 1
       else:
              return n*factorial(n-1)

#To obtain the digits one by one and adding them
while num//10>0:
       n=num%10
       total+=factorial(n)
       num//=10
total+=factorial(num)

if total==org_num:
       print(f"Yes, {org_num} is a strong number.")
else:
       print(f"No, {org_num} is not a strong number.")
