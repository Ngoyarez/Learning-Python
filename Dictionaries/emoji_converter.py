message = input("Enter your message: \n> ")
words = message.split(' ')
# print(words)
emojis = {
    ":)": "😊",
    "):": "😞"
}
output = ''
for word in words:
    output += emojis.get(word, word) + " "# The get method returns the default word
print(output)

