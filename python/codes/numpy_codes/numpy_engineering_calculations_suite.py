import numpy as np


def get_values():
    """Get multiple numerical values from the user."""
    
    values_input = input(
        "Enter values separated by spaces: "
    )

    return np.array([float(value) for value in values_input.split()])


def kinetic_energy(mass, velocity):
    """Calculate kinetic energy for multiple velocity values."""
    
    return 0.5 * mass * velocity ** 2


def dynamic_pressure(density, velocity):
    """Calculate dynamic pressure for multiple velocity values."""
    
    return 0.5 * density * velocity ** 2


def momentum(mass, velocity):
    """Calculate momentum for multiple velocity values."""
    
    return mass * velocity


print("========== NUMPY ENGINEERING CALCULATION SUITE ==========")

while True:

    print()
    print("1. Kinetic Energy")
    print("2. Dynamic Pressure")
    print("3. Momentum")
    print("4. Array Information")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # --------------------------------------------------
    # KINETIC ENERGY
    # --------------------------------------------------

    if choice == "1":

        print()
        print("----- KINETIC ENERGY -----")

        mass = float(input("Enter mass in kg: "))

        velocity = get_values()

        result = kinetic_energy(mass, velocity)

        print()
        print("Velocity:", velocity)
        print("Kinetic Energy:", result, "J")

    # --------------------------------------------------
    # DYNAMIC PRESSURE
    # --------------------------------------------------

    elif choice == "2":

        print()
        print("----- DYNAMIC PRESSURE -----")

        density = float(input("Enter air density in kg/m^3: "))

        velocity = get_values()

        result = dynamic_pressure(density, velocity)

        print()
        print("Velocity:", velocity)
        print("Dynamic Pressure:", result, "Pa")

    # --------------------------------------------------
    # MOMENTUM
    # --------------------------------------------------

    elif choice == "3":

        print()
        print("----- MOMENTUM -----")

        mass = float(input("Enter mass in kg: "))

        velocity = get_values()

        result = momentum(mass, velocity)

        print()
        print("Velocity:", velocity)
        print("Momentum:", result, "kg·m/s")

    # --------------------------------------------------
    # ARRAY INFORMATION
    # --------------------------------------------------

    elif choice == "4":

        print()
        print("----- ARRAY INFORMATION -----")

        values = get_values()

        print()
        print("Array:", values)
        print("Shape:", values.shape)
        print("Size:", values.size)
        print("Number of dimensions:", values.ndim)
        print("Maximum value:", np.max(values))
        print("Minimum value:", np.min(values))
        print("Average value:", np.mean(values))

    # --------------------------------------------------
    # EXIT
    # --------------------------------------------------

    elif choice == "5":

        print()
        print("Exiting program...")
        break

    else:

        print()
        print("Invalid choice. Please try again.")