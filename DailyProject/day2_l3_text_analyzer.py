text = input("Enter a block of text for analysis:")

num_of_char = len(text)

print("Total Characters: ", num_of_char)

words = text.split(" ")
words_n = []
for word in words:
    word = word.strip('.')
    word = word.strip('(')
    word = word.strip('),')
    words_n.append(word)

print("Total Words: ", len(words_n))

sen = text.split(". ")

print("Total Sentences: ", len(sen))

