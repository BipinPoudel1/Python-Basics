#Write a Python function to find the largest number in a list.

def largest_number(givenList):
      new_List= givenList[0]

      for item in givenList:
            if new_List<item:
                  new_List=item
      
      return new_List

print("Largest number in the list is ", largest_number([40, 59, 97, 5, 100]))
