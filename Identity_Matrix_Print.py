# Program to Print an Identity Matrix

n = int(input("Enter the number: "))
for i in range(n):
    for j in range(n):
        if i == j:
            print('1', sep=" ",end=" ")
        else:
            print("0",sep=" ",end=" ")
    print()