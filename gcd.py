#Write a Python program to find the Greatest Common Divisor (GCD) of two numbers.

n1= int(input("Input a number- "))
n2= int(input("Input another number- "))

n1=abs(n1)
n2= abs(n2)

if n1>n2:
       n1, n2= n2, n1

if n1==0 and n2==0:
       print("Undefined.")
       exit(0)
elif n1==0:
       print(f"{n2} is the GCD of given numbers.")
       exit(0)
elif n2==0:
       print(f"{n1} is the GCD of given numbers.")
       exit(0)

while n2%n1>0:
       r= n2%n1
       n2=n1
       n1=r

print(f"{n1} is the GCD of given numbers.")