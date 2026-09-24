'''Welcome to the Power Calculator!'''
print('-' * 50)
print("This program calculates the power")
print('-' * 50)

#Inputs
Work = float(input("Enter the work done (in joules): "))
Time = float(input("Enter the time taken (in seconds): "))

#Calculations
def calculate_power(work, time):
    if time <= 0 or work <= 0:
        return None
    power = work / time
    return power

#Output
result = calculate_power(Work, Time)
if result is not None:
    print(f"The power is: {result:.4f} Watts")
else:
    print("Error: Work and time must be positive values.")