#Write a Python program to count the occurrences of each character in a string
#My way
word= input("Input any word- ")
newSet= set(word)

for i in newSet:
      print(f"'{i}' = {word.count(i)}")
#Less efficient as it scans the entire string for each character again and again.


#Sky way
# word= input("Input any word- ")
# frequency= {}

# for char in word:
#       if char in frequency:
#             frequency[char] += 1
#       else:
#             frequency[char]=1

# for key, value in frequency.items():
#       print(f"'{key}' = {value}")