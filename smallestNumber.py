#Write a Python program to find the smallest number in a list.

n= int(input("How many numbers do you want to input?"))
numbers= [int(input("Enter  numbers- ")) for i in range(n)]

smallest= numbers[0]

for item in numbers:
       if item<smallest:
              smallest=item

print("Smallest~ ", smallest)