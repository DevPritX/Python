# Python Variables

# Variables: Variable are containers for storing data values.

# Creating variables:

#   Python has no command to declaring a variable.
#   A variable is created the moment you first assign a value to it.

# ex:

x = 5
y = "John"

print(x)
print(y)

# In Python variables do not need to be declared with any particular type, and can even change type after they have been set
# ex:

x = 4       # x is now int
x = "Sally" # x is now str

print(x)    # Sally

# Single Or Double Quotes?

# String variable can be declared either by using single ('') or double ("") quotes:
# ex:

x = 'John'
x = "John"  # This x variable value is same as before

# Case Sensitive

#Variable names are case-sensitive
# ex:

a = 4
A = "Sally"

# Here 'A' will not overwrite 'a' soo 'A' and 'a' are different variables with different value

print(a)
print(A)