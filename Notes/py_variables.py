# Python Variables

# Variables: Variable are containers for storing data values.

# Creating variables:

#   Python has no command to declaring a variable.
#   A variable is created the moment you first assign a value to it.

# Ex:

x = 5
y = "John"

print(x)
print(y)

# In Python variables do not need to be declared with any particular type, and can even change type after they have been set
# Ex:

x = 4       # x is now int
x = "Sally" # x is now str

print(x)    # Sally

# Single Or Double Quotes?

# String variable can be declared either by using single ('') or double ("") quotes:
# Ex:

x = 'John'
x = "John"  # This x variable value is same as before

# Case Sensitive

#Variable names are case-sensitive
# Ex:

a = 4
A = "Sally"

# Here 'A' will not overwrite 'a' soo 'A' and 'a' are different variables with different value

print(a)
print(A)

# ! ------------------------------------------

# Python - Variable Names

# Variable names: A variable can have a short name (like x and y) or a more descriptive name (like age, carname, total_volume).

# ! Rules for Python variables

#   A variable name must start with a letter or the underscore character
#   A variable name cannot start with a number
#   A variable name can only contain alpha-numeric characters and underscores ( A-z, 0-9, and _ )
#   Variable names are case sensitive (age, Age, and AGE are three different variables)
#   A variable name cannot br any of the 'Python Keywords'

# Ex:

# ? These all variables are legal and different than others

myvar = "John"  # ✅

myVar = "John"  # ✅

MYVAR = "John"  # ✅

my_var = "John"  # ✅

_my_var = "John"  # ✅

myVar2 = "John"  # ✅

# ? These all are illegal variable names

2myvar = "Sally" # ❌

my-var = "Sally" # ❌

my var = "Sally" # ❌


# ! Also remember variable names are case-sensitive


# * Multi-words  variable names:
# ? Variable names more than one word can be difficult to read.
# ? There are several techniques you can use to make them more readable.

#? 1. Camel Case:
# Each word, except the first, starts with a capital letter:
# Ex:

myVarName = "john"
yourFirstName = "Tommy"

#? 2. Pascal Case:
# Each word starts with a capital letter
# Ex:

MyVarName = "John"
YourFirstName = "Tommy"

#? 3. Snake Case:
# Each word is separated by an underscore character
# Ex:

my_var_name = "John"
your_first_name = "Tommy"


# ! ------------------------------------------

#* Python Variables - Assign Multiple Values

#? 1. Many values to multiple variables
#   Python allows you to assign values to multiple variables in one line:
#Ex:

x, y, z = "Orange", "Banana", "Cherry"

print(x) # Orange
print(y) # Banana
print(z) # Cherry

#! Note: Make sure the number of variables matches the number of values, or else you will get an error.


#? 2. One value to multiple variables
#   And you can assign the same value to multiple variables in one line:
# Ex:

x = y = z = "Orange"

print(x) # Orange
print(y) # Orange
print(z) # Orange


#? 3. Unpack a Collection
#   If you have collection of values in a list, tuple etc, Python allows you to extract the values into variables. This is called 'Unpacking'.
# Ex:

#? Unpack a list

fruits = ["apple", "banana", "cherry"]  # This is a list

x, y, z = fruits    # Unpacking the multiple values from a list into multiple variables.

print(x) # apple
print(y) # banana
print(z) # cherry

# TODO: Learn more about unpacking

# ! ------------------------------------------

#? Python - Output Variables

#* Output variables: The Python print() function is often used to output variables.
# Ex:

x = "Python is awesome"
print(x) # Python is awesome

#? In print() function you can output multiple variables, separated by commas (','):
# Ex:

x = "Python"
y = "is"
z = "awesome"

print(x, y, z) # Python is awesome

# You can also use the '+' operator to output multiple variables:
# Ex:

x = "Python "
y = "is "
z = "awesome"

print(x + y + z) # Python is awesome

# But if you want's to skip whitespace after "Python " & "is " let's see a result:
# Ex:

x = "Python"
y = "is"
z = "awesome"

print(x + y + z) # Pythonisawesome

#! Note: This happens because '+' operator is concantanate if the variables are "string" data type

#! Note: For numbers the "+" character works as mathematical operator:
# Ex:

x = 10
y = 20

print(x + y) # 30

# But in print() function when you try to combine a number and a string with the "+" operator, Python will give you an error:
# Ex:

x = 5
y = "John"

print(x + y) #! Error

#! Note: The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
# Ex:

x = 5
y = "John"

print(x, y) # 5 John

#* Python - Global Variables:
#? Global variables:
# Variables that are created outside of a function are known as Global Variables.
# Global variables can be used by everyone, both inside and outside of a function.
# Ex:

#! Create a variable outside of function, and use it inside the function.

x = "awesome"

def myFunction():
    print("Python is", x)

myFunction() # Python is awesome

#? If you create a variable with the same name inside of a function, this variable will be local, and can only be used inside the function. The global variable with same name will remain as it was, global and with the original value.

# Ex:

x = "awesome"

def myFunction():
    x = "fantastic"
    print("Python is", x) # Python is fantastic

myFunction()

print("Python is", x) # Python is awesome

#* The Global Keyword

#? Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
#? To create a global variable inside a function, you can use the global keyword.
# Ex:

def myFunction():
    global x    #? If you use the global keyword, the variable belongs to the global scope.
    x = "fantastic"

myFunction()

print("Python is " + x)

#? Also use the global keyword if you want to change a global variable inside a function.
#? To change the value of global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myFunction():
    global x
    x = "fantastic"

myFunction()

print("Python is " + x)