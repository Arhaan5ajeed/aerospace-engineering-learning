'''Welcome toPressure Calculator'''

print('-' * 50)
print("Pressure Calculator")
print('-' * 50)

#Inputs
force = float(input("Enter the force in newtons: "))
area = float(input("Enter the area in square meters: "))

#Defining function to calculate pressure
def calculate_pressure(force, area):
    if area <= 0:
        return None
    pressure = force / area
    return pressure

#output
pressure = calculate_pressure(force, area)
if pressure is not None:
    print(f"The pressure is: {pressure:.4f} N/m^2")
else:
    print("Error: Area must be greater than zero.")