#Write a function to check whether a string is a palindrome.

def isPalindrome (text):
       text= text.lower()
       reversed_text= text[::-1]

       if text==reversed_text:
              return True
       else:
              return False

text= input("Enter any word~ ")
print(f"{text} is palindrome? {isPalindrome(text)}")