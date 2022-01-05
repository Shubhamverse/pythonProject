# Program to Read a File and Capitalize the First Letter of Every Word in the File

filename = input("Enter the file name: ")  # test.txt was input

with open(filename, 'r') as f:
    for line in f:
        l = line.title()
        print(l)