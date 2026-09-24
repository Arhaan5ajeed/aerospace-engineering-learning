'''Welcome to the stress calculator!'''
print('-' * 50)
print("This program calculates the stress")
print('-' * 50)

#Inputs
Force = float(input("Enter the force applied (in newtons): "))
Area = float(input("Enter the area over which the force is applied (in square meters): "))

#Calculations
def calculate_stress(force, area):
    if area <= 0:
        return None
    stress = force / area
    return stress

#Output
result = calculate_stress(Force, Area)
if result is not None:
    print(f"The stress is: {result:.4f} Pascals")
else:
    print("Error: Area must be a positive value.")