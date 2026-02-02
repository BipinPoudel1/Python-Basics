#Python program to check if the given number is prime or not.

num = int(input("You give me one number- "))

if num == 0 or num == 1:
    print(f"{num} is neither prime nor composite.")
elif num == 2:
    print(f"{num} is a prime number.")
else:
    for i in range(2, int(num**0.5) + 1):  
        if num % i == 0:
            print(f"{num} is a composite number.")
            break
    else:
        print(f"{num} is a prime number.")
