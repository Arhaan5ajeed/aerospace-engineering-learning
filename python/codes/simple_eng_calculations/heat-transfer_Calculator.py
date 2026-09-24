'''Water Heat Transfer Calculator'''
print('-' * 50)
print("This program calculates the heat transfer")
print('-' * 50)

# Inputs
mass = float(input("Enter the mass of the water (in kilograms): "))
specific_heat = float(input("Enter the specific heat capacity of (in J/kg°C): "))
temp1 = float(input("Enter the initial temperature of the water (in °C): "))
temp2 = float(input("Enter the final temperature of the water (in °C): "))

# Calculations
def calculate_heat_transfer(mass, specific_heat, temp1, temp2):
    if mass <= 0 or specific_heat <= 0:
        return None
    heat_transfer = mass * specific_heat * (temp2 - temp1)
    return heat_transfer

# Output
result = calculate_heat_transfer(mass, specific_heat, temp1, temp2)
if result is not None:
    print(f"The heat transfer is: {result:.4f} Joules")
else:
    print("Error: Mass and specific heat capacity must be positive values.")
    