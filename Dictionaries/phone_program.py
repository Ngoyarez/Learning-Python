phone = input("Phone Number: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " " # The get method prevents the program from yelling at the user when
                                                # a key doesn't exists in the input. We can also give a default value
                                                # as the second object
print(output)

