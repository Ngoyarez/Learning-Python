course = 'Python for Beginners'
print(len(course))       # Prints the number of characters in the string. len is a function like print and input
print(course.upper())    # Prints all the characters of the string in upper case.
                         # This method does not modify the original string
# print(course)
print(course.lower())    # Prints all the characters of the string in lowercase
print(course.find('P'))  # Prints the index of the first occurrence of the given character and it is case sensitive
print(course.find('Beginners'))  # Prints the index of the first occurrence of character B
print(course.replace('Beginners', 'Absolute Beginners')) # Replaces the word in the string with the given new word
                                                         # and it is case sensitive
print(course.replace('P', 'J')) # Replaces the character with the new character
print('Jython' in course) # Finds if the given character or word exists in the string. Returns a boolean value
# print(course)
