#Write a Python program to count the frequency of each word in a given sentence.

sentence= input("The sentence is ...")
word_wise= sentence.split(" ")

frequency= {}

for word in word_wise:
       if word in frequency:
              frequency[word]+=1
       else:
              frequency[word]=1

print(frequency)