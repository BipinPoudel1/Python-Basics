#Write a Python program to check whether a given string is a pangram.
#Hint: A pangram is a sent that contains every letter of the alphabet at least once.

alphabets=set( 'abcdefghijklmnopqrstuvwxyz')
sent= set(input("Write your sent- ").lower().replace(" ", ""))

if alphabets.issubset(sent):
       print("Pangram")
else:
       print("Not Pangram")



