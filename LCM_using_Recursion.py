# Find the LCM of Two Numbers Using Recursion

#problematic unsolved

def lcm(a, b):
    temp = temp + b
    if temp % a == 0 and temp % b == 0:
        return temp
    else:
        lcm(a, b)
    return temp


temp = 0
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if a > b:
    lcm1 = lcm(b, a)
else:
    lcm1 = lcm(a, b)
print("LCM is ", lcm1)