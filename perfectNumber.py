#perfect number check
#number that is the sum of it's divisors.

print("Perfect Number checker")
num= int(input("Enter any number~ "))
total=0
for i in range (1, (num//2)+1):
       if num%i==0:
              total+=i
if total==num:
       print(f"Yes, {num} is a perfect number.")
else:
       print(f"No, {num} is not a perfect number.")