# Program to Count the Number of Blank Spaces in a Text File

filename = input("Enter the file name: ")
k = 0
with open(filename, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if letter.isspace:
                    k = k + 1
print(f"Space occured in file {k} times. ")
