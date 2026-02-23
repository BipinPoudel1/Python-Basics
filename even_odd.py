#Write a function that checks if a number is even or odd.

def evenOdd(num):
      if (num%2)==0:
            print(f"{num} is an even number.")
      else:
            print(f"{num} is an odd number.")

num= int(input("Enter any number~ "))
evenOdd(num)


