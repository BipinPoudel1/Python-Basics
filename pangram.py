#Write a Python program to check whether a given string is a pangram.
#Hint: A pangram is a sentence that contains every letter of the alphabet at least once.

alphabets=set( 'abcdefghijklmnopqrstuvwxyz')
sentence= set(input("Write your sentence- ").lower().replace(" ", ""))

if alphabets.issubset(sentence):
       print("Pangram")
else:
       print("Not Pangram")



