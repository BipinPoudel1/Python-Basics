#Number Guessing Game

import random, math
print("~~~~~ Welcome to the NUMBER GUESSING GAME  ~~~~~")
number= math.ceil(random.random()*100)

count=0

while True:
       count+=1
       guess= int(input("Guess the number_ "))
       if number>guess:
              print("The number is greater than the guessed number.")
       elif number<guess:
              print("The number is lesser than the guessed number.")
       else:
              print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
              print("You guessed it right.")
              print(f"Number= {number}")
              print(f"Attempts= {count}")
              print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
              break


