'''Welcome toHydrostatic Pressure Calculator'''

print('-' * 50)
print("Hydrostatic Pressure Calculator")
print('-' * 50)

#Inputs
density = float(input("Enter the density of the fluid in kg/m^3: "))
gravity = 9.81  # Acceleration due to gravity in m/s^2
depth = float(input("Enter the depth of the fluid in meters: "))

#Defining function to calculate hydrostatic pressure
def calculate_hydrostatic_pressure(density, gravity, depth):
    if depth <= 0 or density <= 0:
        return None
    pressure = density * gravity * depth
    return pressure

#output
pressure = calculate_hydrostatic_pressure(density, gravity, depth)
if pressure is not None:
    print(f"The hydrostatic pressure is: {pressure:.4f} N/m^2")
else:
    print("Error: Depth and density must be greater than zero.")