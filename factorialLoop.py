#Write a Python program to calculate the factorial of a given number using a loop.

num= int(input("Enter a number "))
ans=1
if num==1 or num==0:
      print("Factorial is 1.")
else:
      for i in range (2, num+1):
            ans= ans*i
      print("Factorial is ", ans)

