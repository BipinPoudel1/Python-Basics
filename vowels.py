#Count the number of vowels in "Artificial Intelligence"

def vowelCounter(text):
      try:
            vowel= "aeiou"
            count= 0
            text= text.lower()
            
            for char in text:
                  if char in vowel:
                        count+=1
            return count
      except Exception as e:
            print(e)

print("Vowels: ", vowelCounter("Artificial Intelligence"))