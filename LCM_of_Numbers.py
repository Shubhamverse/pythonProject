#Python Program to Find the LCM of Two Numbers

x= int(input("Enter the first number :"))
y =int(input("Enter the second number :"))
if x>y:
    min_num = x
else:
    min_num =y
while(1):
    if(min_num%x==0 and min_num%y==0):
        print("LCM is :", min_num)
        break
    min_num =min_num +1