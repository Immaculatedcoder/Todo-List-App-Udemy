filenames = ['a.txt', 'b.txt', 'c.txt']


for files in filenames:
    file = open(files, "r")
    output = file.read()
    print(output)

