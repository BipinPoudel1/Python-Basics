#Write a Python program that takes two lists and returns a list of elements that appear in both lists.

#My Way
list1= [5, 8, 2]
list2= [5, 6, 3]
resultantList= []

for i in list1:
      for j in list2:
            if i==j and i not in resultantList:
                  resultantList.append(i)

print("Common element(s)- ", resultantList)


#Sky Way
# list1= [2, 5, 8]
# list2= [3, 5, 6]
# common= list(set(list1) & set(list2))
# print(common)