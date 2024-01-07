
# If you want to write a string with a single quote in it, you need to enclose the string
# with double quotes and vice versa

# To define a string with multiple lines, you use triple quotes
# Example
message = '''
Hi, Brian

Here is our first course offer to you

Thank You,
The support team

'''



print(message)

course = "Python For Beginners"
another = course[:]
print(course[0])   # Prints the character of the first index
print(course[-1])  # Prints the character of the last index
print(course[0:3]) # Prints the character at index 0 to 2
print(course[1:])  # Prints all the characters excluding the first character
print(course[:5])  # Prints all the characters excluding the character at index 5 (0 - 4)
print(course[:])   # Prints all the characters of the string - simple way to copy or clone a string

name = 'Jennifer'
print(name[1:-1])





