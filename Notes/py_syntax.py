# Python Syntax

# Python Indentation

#   Indentation refers to the spaces at the beginning of a code line.
#   Where in other programming languages the indentation in code is for readability only, the indentation in python is very important.

# Python uses indentations to indicate a block of scope:
# Ex:

if 5 > 2:
    print("Five is grater than two")

# Python will give you an error if you skip the indentation:

# Ex:

if 5 > 2:
print("Five is greater than two")

# The number of spaces up to you as a programmer, the most common use is four, but it has to be at least one.
# Ex:
if 5 > 2:
 print("Five is greater than two")
if 2 < 5:
        print("Two is less than Five")

# You have to use the same number of spaces in the same block of code, other wise Python will give you error:
# Ex:

# Right way ✅

if 5 > 2:
 print("Five is greater than two")
 print("Five is greater than two")

# Wrong way ❌
if 5 > 2:
 print("Five is greater than two")
    print("Five is greater than two")
        print("Five is greater than two")