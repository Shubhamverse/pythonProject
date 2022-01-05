#Remove the nth Index Character from a Non-Empty String

def remove (string1, n):
    first = string1[:n]
    second = string1[n+1:]
    string2 = first + second
    return string2

string1 = input("Enter the string: ")
n = int(input("Enter the index of element to remove from the string:"))

print("New string:")
print(remove(string1 , n))