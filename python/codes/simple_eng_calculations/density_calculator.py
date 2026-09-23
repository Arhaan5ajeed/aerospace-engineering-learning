'''Welcome to Density Calculator'''

print('-' * 50)
print("Density Calculator")
print('-' * 50)

#Inputs
mass = float(input("Enter The mass in kilograms"))
volume = float(input("Enter the volume in cubic meters: "))

#Defining function to calculate density
def calculate_density(mass, volume):
    if volume <= 0 or mass <= 0:
        return None
    density = mass / volume
    return density

#output
density = calculate_density(mass, volume)
if density is not None:
    print(f"The density is: {density:.4f} kg/m^3")
else:
    print("Error: Volume and mass must be greater than zero.")