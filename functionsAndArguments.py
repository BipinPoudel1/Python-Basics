#Function Arguments
##There are four types of arguments that we can provide in a function:

#1. Default Arguments
def average(a=9,b=1):
        print("The average is ", + (a+b)/2)

average() #Gives the average of 9 and 1
average(4) #Gives the average of a=4 and b=1 as only 4 is passed when the function is called
average(b=6) #Gives the average of 9 and 6 as default a=9 and given b=6
average(9,9) #Gives the average of what is given (as both arguments are passed)

#2. Keyword Arguments - when we give arguments as a key-value pair, the order doesn't matter. 
average(b=7, a=21) #In this case, the order is (b,a) but the value is recognized and the interpreter automatically assigns a=21 and b=7

#3. Required Arguments
#It is the type of argument where it is mandatory to give the parameter as asked by the function. Either it can be one argument, or two, or more, if it is defined as 

def name(fname, mname, lname):
        print("Hello", fname, mname, lname)

#name("Peter", "Quill")  #It will throw error as 'lname' is also a required argument. So, we have to provide value to all three arguments as
name ("Peter", "Starlord", "Quill")

#4. Variable-length argument
#Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments. There are two ways to achieve this:
#Arbitrary Arguments:
#While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of tuple.
def sum(*number):
        add=0
        for i in number:
                add+=i
        print(add)
sum(1, 2, 5) #The number of the arguments passed can be 'any' now

#Keyword Arbitrary Arguments
def greet(**names):
        print("Hello there Mr.", names["fname"], names["mname"], names["lname"])

greet(mname="Buchanan", fname="James", lname="Barnes")