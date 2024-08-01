# Python Comments

#   Comments can be used to explain python code.
#   Comments can be used to make the code more readable.
#   Comments can be used to prevent execution when testing code.

# Creating comment in Python

# Comments Starts with a '#', and Python will ignore them:
# Ex:

# This is a comment
print("This is not a comment")

# Comments can be placed at the end of a line, and Python will ignore the rest of the line:
# Ex:

print("Hey, i am busy now") # This is a Comment

# A Comment does not have to be text that explains the code, it can also be used to prevent python from executing the code:

# print("This line of code will be ignored by python")
print("This will be printed")

# Multiline comments in Python

#   Python does not really have a syntax for multiline comments.

# To add a multiline comment you could insert a # for each line:
# Ex:

# This is a Comment
# This is a new Comment
# This is a another new comment

# Also there is a another way to create multiline comments. You can use multiline string.
# Since Python will ignore string literals that are not assigned to a variable, you can add a multiline string (triple quotes) in your code, and place your comment inside it.
#Ex:

"""
    This is 1st line
    This is 2nd line
    This is 3rd line
    This also last line.
"""
print("Hello, world!")
'''
    This is 1st line
    This is 2nd line
    This is 3rd line
    This also last line.
'''
print("Hello, world!")

# As long as the string is not assigned to a variable, Python will read the code, but then ignore it, and you have made a multiline comment

# Also You create single line comment using "", '' quotes
# Ex:
"Hii There How are You?"
"I am Fine, Or you?"

print("Hello, world!")
