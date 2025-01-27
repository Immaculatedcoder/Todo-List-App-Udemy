filenames = ["1.doc", "1.report", "1.presentation"]

new_filenames = [file.replace('.', '-') + ".txt" for file in filenames]

print(new_filenames)