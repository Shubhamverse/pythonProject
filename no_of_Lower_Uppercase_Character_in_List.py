#Calculate the Number of Upper Case Letters and Lower Case Letters in a String

string1 = input("Enter the string: ")
count1 = 0
count2 = 0
for i in string1:
    if i == i.lower():
        count1 = count1 + 1
    else:
        count2 = count2 + 1

print("Number of uppercase character in string is ",count2)
print("Number of lowercase characters in string is ", count1)