#Use list comprehension to create a list of squares of numbers from 1 to n.
#My Way
# n= int(input("Give n: "))
# myList=[]
# for i in range (0, n):
#        n2= int(input((f"Give {i+1}th number: ")))
#        myList.append(n2)

# squaredList= [i**2 for i in myList]
# print("Squares of the given numbers are: ")
# print(squaredList)

#Sky Way
n= int(input("Enter n: "))
squares= [i**2 for i in range(1, n+1)]
print(squares)