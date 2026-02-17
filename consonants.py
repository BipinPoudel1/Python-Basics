#Count the number of consonants in a string.

def counter(text):
      text= text.lower()
      count= 0
      vowels= "aeiou"

      for char in text:
            if char.isalpha() and char not in vowels:
                  count+=1
      return count

text= input("Input your desired string~ ")
print(f"Number of consonents in {text} is {counter(text)}")