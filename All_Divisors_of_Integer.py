#Generate all the Divisors of an Integer

num = int(input("Enter the integer: "))
print(f"The divisors of {num} are:")
for i in range(1,num+1):
    if num%i==0:
        print(i)