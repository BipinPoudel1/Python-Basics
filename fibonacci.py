#Write a Python function that returns the Fibonacci sequence up to n terms.

def fibonacci(n):
      a= 0
      b= 1

      if n<=0:
            print("Give positive number- ")
            exit(1)
      elif n==1:
            return a
      else:
            print(a)
            print(b)

            for i in range (2, n):
                  c= a+b
                  a=b
                  b=c
                  print(c)

n= int(input("Please give any number_ "))
fibonacci(n)

