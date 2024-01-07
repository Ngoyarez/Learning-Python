numbers = [5, 2, 3, 4, 5]
numbers.append(6) # Adds a number or a character to the end of the list
print(numbers)

numbers.insert(0, 8) # Inserts a number at a given index: index, object
print(numbers)

numbers.remove(5) #Remove the first occurence of the number 5
print(numbers)

# numbers.clear() # completely remove all the elements of a list
# print(numbers)

numbers.pop() # Remove the last item of a list
print(numbers)

numbers.index(5) # Checks for the existence of a number in a list. Returns the first occurence of the number
print(numbers)

numbers.count(5) # Return the times of occurence of a number
print(numbers)

numbers.sort() # Sorts the list in asccending order
print(numbers)

numbers.reverse() # Sort the list in descending order
numbers.copy # Copy an existing list
numbers2 = numbers.copy()
numbers.append(10)