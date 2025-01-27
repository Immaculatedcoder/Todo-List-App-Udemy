contents = ["All carrots are to be sliced longitudinally.",
            "The carrots were reportedly sliced",
            "The slicing process was well presented."]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

# for index, name in enumerate(filenames):
#     file = open(name, 'w')
#     file.writelines(content[index])
#     file.close()


for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", 'w')
    file.writelines(content)
    file.close()