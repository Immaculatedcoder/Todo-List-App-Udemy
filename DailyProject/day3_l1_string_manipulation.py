name = input("Please enter your full name: ")

print("Your name in uppercase: ", name.upper())
print("Your name in lowercase: ", name.lower())

char_name = name.replace(" ", "") # Here I'm removing the spacing between the characters
characters = []
for i in char_name:
    characters.append(i)

print("Total number of characters (excluding spaces): ", len(characters))


print("Your name reversed: ", name[::-1])





