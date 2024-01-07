# numbers = [1, 4]
# if numbers[0] < numbers[1]:
#     print(f"{numbers[1]} is greater than {numbers[0]} ")


numbers = [1, 3, 8, 4, 6, 9]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(max)