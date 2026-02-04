#Write a program to check whether a number is a palindrome.

print("Palindrome checker")
num= int(input("You, yes you, give me a number and I will tell you if that number is palindrome or not? C'mon give me..."))

if num<0:
       print("The given number is invalid. Only positive number is valid.")
else:
       num_str= str(num)
       rev_num=num_str[::-1]
       
       if num_str==rev_num:
              print(f"Yes,{num} is a palindrome number.")
       else:
              print(f"No, {num} is not a palindrome number.")
