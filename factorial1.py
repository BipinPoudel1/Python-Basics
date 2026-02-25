#Write a Python function to find the factorial of a number using recursion.

def factorial (n):
       if n<0:
              return f"Undefined"
       elif n==0 or n==1:
              return 1
       else:
              return n*factorial(n-1)

n= int(input("Give a number to find the factorial~ "))
print(f"Facrorial of {n} = {factorial(n)}")
       