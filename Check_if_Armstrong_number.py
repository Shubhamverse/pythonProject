#Check if a Number is an Armstrong Number

num = int(input("Enter the number: "))
a= list(map(int,str(num)))
b= list(map(lambda x:x**3,a))
if sum(b)==num:
    print("The number is Armstrong Number. ")
else:
    print("The number is not Armstrong Number. ")