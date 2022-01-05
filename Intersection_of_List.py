# Find the Intersection of Two Lists

def intersection(list1, list2):
    return list(set(list1) & set(list2))  #intersection of sets


num1 = int(input("Enter the length of first list: "))
list1 = []
for i in range(num1):
    elem1 = int(input("Enter the element of the First List: "))
    list1.append(elem1)
num2 = int(input("Enter the length of second list: "))
list2 = []
for j in range(num2):
    elem2 = int(input("Enter the element of the Second List: "))
    list2.append(elem2)
print("The first list:", list1)
print("The second list:", list2)
print("The intersection of the list: ")
print(intersection(list1, list2))