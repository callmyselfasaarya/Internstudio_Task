c = 0

# Opening our text file in read only mode
with open(r'ExampleText.txt','r') as file:
    data = file.read()
    lines = data.split()

    # Iterating over every word in lines
    for word in lines:

        # checking if the word is numeric or not
        if not word.isnumeric():

            c += 1

print("The Total count of word in the text file is",c)