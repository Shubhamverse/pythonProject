# Check If Two Numbers are Amicable Numbers

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

sum1 = 0
sum2 = 0
for i in range(1, a):
    if a % i == 0:
        sum1 += i
for j in range(1, b):
    if b % j == 0:
        sum2 += j
if sum1 == b and sum2 == a:
    print("Amicable")
else:
    print("Not Amicable")
