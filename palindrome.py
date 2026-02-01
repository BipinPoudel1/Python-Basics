#Q1. Write a function that checks whether a string is a palindrome (reads the same forward & backward).


#My Version
# def isPalindrome (text):
#       text= text.lower()
#       rev_text= text[::-1]
      
#       if text==rev_text:
#             return True
#       else:
#             return False

# text= input("Enter any string~ ")
# print(f"Is {text} palindrome? The answer is {isPalindrome(text)}")


#/Shorter Method - suggested by ChatGPT
def isPalindrome(text):
      text= text.lower()

      return text==text[::-1]
print(f"Is palindrome? The answer is {isPalindrome("madam")}")
