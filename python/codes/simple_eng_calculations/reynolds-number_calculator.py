'''Welcome to Reynolds Number Calculator and Flow Regime Determination'''

print('-' * 50)
print("Reynolds Number Calculator")
print('-' * 50)

#Inputs
fluid_density = float(input("Enter the density of the fluid in kg/m^3: "))
fluid_velocity = float(input("Enter the velocity of the fluid in m/s: "))
fluid_dynamic_viscosity = float(input("Enter the dynamic viscosity of the fluid in Pa.s: "))
pipe_length = float(input("Enter the characteristic length of the pipe in meters: "))

#Defining function to calculate Reynolds number
def calculate_reynolds_number(density, velocity, length, viscosity):
    if length <= 0 or viscosity <= 0 or density <= 0 or velocity <= 0:
        return None
    reynolds_number = (density * velocity * length) / viscosity
    return reynolds_number
reynolds_number = calculate_reynolds_number(fluid_density, fluid_velocity, pipe_length, fluid_dynamic_viscosity)

#Output
if reynolds_number is not None:
    print(f"The Reynolds number is: {reynolds_number:.4f}")

    # Determine the flow regime
    if reynolds_number < 2000:
        print("The flow is laminar.")
    elif reynolds_number > 4000:
        print("The flow is turbulent.")
    else:
        print("The flow is in the transition zone.")
else:
    print("Error: All inputs must be positive values.")