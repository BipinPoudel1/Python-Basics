#Write a Python program to generate the first n terms of the Fibonacci sequence.

n= int(input("Enter 'n'~ "))
fibonacci= [0, 1]

if n<=0:
       print("Give valid number of terms.")
elif n==1:
       print(fibonacci[0])
elif n==2:
       print(fibonacci)
else:
       for i in range (1, n-1):
              num= fibonacci[i]+fibonacci[i-1]
              fibonacci.append(num)
       print(f"Fibonacci sequence upto {n} terms is {fibonacci}")
