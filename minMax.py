#Write a Python function to find the maximum and minimum numbers in a list.

def minMax(givenList):
       minNum= min(givenList)
       maxNum= max(givenList)

       return f"{minNum}, {maxNum}"

givenList= [10, 10, 2]
print(f"{minMax(givenList)} is the minimum and maximum numbers of the list respectively.")