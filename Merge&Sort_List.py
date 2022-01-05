#Merge Two Lists and Sort it

num1 = int(input("Enter the length of first List: "))
list1 =[]
for i in range(num1):
    elem1 = int(input("Enter the Elements of List: "))
    list1.append(elem1)
num2 = int(input("Enter the length of second List: "))
list2 =[]
for i in range(num2):
    elem2 =int(input("Enter the elements of  List: "))
    list2.append(elem2)

sorted_list = list1 + list2
sorted_list.sort()
print("The Merged And Sorted List: ", sorted_list)