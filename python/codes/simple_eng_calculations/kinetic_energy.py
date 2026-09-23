'''
Kinetic Energy Calculation Module
'''

print('-' * 50)
print("Kinetic Energy Calculation Module Loaded")
print('-' * 50)

#inputs
mass = float(input("Enter the mass in kilograms: "))
velocity = float(input("Enter the velocity in meters per second: "))

#defining function to calculate kinetic energy
def calculate_kinetic_energy(mass, velocity):
    if mass <= 0 or velocity < 0:
        return None
    kinetic_energy = 0.5 * mass * velocity ** 2
    return kinetic_energy
kinetic_energy = calculate_kinetic_energy(mass, velocity)

#output
if kinetic_energy is not None:
    print(f"The kinetic energy is: {kinetic_energy:.4f} Joules")
else:
    print("Error: Mass and velocity cannot be negative.")