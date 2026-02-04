#Write a Python program to check whether a number is an automorphic number or not.

print("Automorphic number checker.")
num= int(input("Input a number- "))
square= num**2
length=len(str(num))

last_digits= square%(10**length)

if num==last_digits:
       print("Automorphic.")
else:
       print("Not an automorphic.")