#Write a Python program to count the frequency of each character in a string.

text= input("You give me a word- ")
frequency= {}

for char in text:
       if char in frequency:
              frequency[char]+=1
       else:
              frequency[char]=1

print(f"Frequency of each characters: \n {frequency}")