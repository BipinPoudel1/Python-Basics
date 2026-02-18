#Write a Python function to check if two strings are anagrams of each other.

def anagram(string1, string2):
      list1= []
      list2= []

      string1= string1.replace(" ", "")
      string2= string2.replace(" ", "")

      length1= len(string1)
      length2= len(string2)
      if length1!=length2:
            return False
            exit(1)

      string1=string1.lower()
      string2=string2.lower()
      
      for char in string1:
            list1.append(char)
            
      for chars in string2:
            list2.append(chars)
            
      list1.sort()
      list2.sort()

      if list1==list2:
            return True
      else:
            return False

string1= input("Enter any word~ ")
string2= input("Enter another word~ ")
print("The two words are anagram is ", anagram(string1, string2))