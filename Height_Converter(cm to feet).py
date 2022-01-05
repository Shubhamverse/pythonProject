#Read Height in Centimeters and then Convert the Height to Feet and Inches

Height_cm = int(input("Enter the Height in Centimeters: "))
height_inches = 0.394 * Height_cm
height_feet = 0.0328 * Height_cm
print("The length in inches ", round(height_inches,2))
print("The height in feet ", round(height_feet,2))
