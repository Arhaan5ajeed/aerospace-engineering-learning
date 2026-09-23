"""
Continuity Equation Solver
Calculates any one missing variable for
compressible or incompressible steady flow.
"""

import math

print("CONTINUITY EQUATION SOLVER")
print("-" * 30)

# Select flow type
flow_type = input(
    "Is the flow compressible or incompressible? "
).strip().lower()


# --------------------------------------------------
# INCOMPRESSIBLE FLOW
# Equation: A1 * V1 = A2 * V2
# --------------------------------------------------

if flow_type == "incompressible":

    print("\nFor incompressible flow:")
    print("A1 * V1 = A2 * V2")
    print("Enter 'none' for the unknown variable.\n")

    # Inputs
    a1_input = input("Enter inlet area A1 (m^2): ").strip().lower()
    v1_input = input("Enter inlet velocity V1 (m/s): ").strip().lower()
    a2_input = input("Enter outlet area A2 (m^2): ").strip().lower()
    v2_input = input("Enter outlet velocity V2 (m/s): ").strip().lower()

    # Convert "none" to None
    a1 = None if a1_input == "none" else float(a1_input)
    v1 = None if v1_input == "none" else float(v1_input)
    a2 = None if a2_input == "none" else float(a2_input)
    v2 = None if v2_input == "none" else float(v2_input)

    variables = [a1, v1, a2, v2]

    # Check that exactly one variable is missing
    if variables.count(None) != 1:
        print("\nError: Exactly ONE variable must be 'none'.")

    else:

        # Calculate missing V2
        if v2 is None:
            v2 = (a1 * v1) / a2
            print(f"\nOutlet velocity V2 = {v2:.3f} m/s")

        # Calculate missing A2
        elif a2 is None:
            a2 = (a1 * v1) / v2
            print(f"\nOutlet area A2 = {a2:.3f} m^2")

        # Calculate missing V1
        elif v1 is None:
            v1 = (a2 * v2) / a1
            print(f"\nInlet velocity V1 = {v1:.3f} m/s")

        # Calculate missing A1
        elif a1 is None:
            a1 = (a2 * v2) / v1
            print(f"\nInlet area A1 = {a1:.3f} m^2")


# --------------------------------------------------
# COMPRESSIBLE FLOW
# Equation: rho1*A1*V1 = rho2*A2*V2
# --------------------------------------------------

elif flow_type == "compressible":

    print("\nFor compressible flow:")
    print("rho1 * A1 * V1 = rho2 * A2 * V2")
    print("Enter 'none' for the unknown variable.\n")

    # Inputs
    rho1_input = input("Enter inlet density rho1 (kg/m^3): ").strip().lower()
    a1_input = input("Enter inlet area A1 (m^2): ").strip().lower()
    v1_input = input("Enter inlet velocity V1 (m/s): ").strip().lower()

    rho2_input = input("Enter outlet density rho2 (kg/m^3): ").strip().lower()
    a2_input = input("Enter outlet area A2 (m^2): ").strip().lower()
    v2_input = input("Enter outlet velocity V2 (m/s): ").strip().lower()

    # Convert "none" to None
    rho1 = None if rho1_input == "none" else float(rho1_input)
    a1 = None if a1_input == "none" else float(a1_input)
    v1 = None if v1_input == "none" else float(v1_input)

    rho2 = None if rho2_input == "none" else float(rho2_input)
    a2 = None if a2_input == "none" else float(a2_input)
    v2 = None if v2_input == "none" else float(v2_input)

    variables = [rho1, a1, v1, rho2, a2, v2]

    # Check that exactly one variable is missing
    if variables.count(None) != 1:
        print("\nError: Exactly ONE variable must be 'none'.")

    else:

        # Calculate missing V2
        if v2 is None:
            v2 = (rho1 * a1 * v1) / (rho2 * a2)
            print(f"\nOutlet velocity V2 = {v2:.3f} m/s")

        # Calculate missing A2
        elif a2 is None:
            a2 = (rho1 * a1 * v1) / (rho2 * v2)
            print(f"\nOutlet area A2 = {a2:.3f} m^2")

        # Calculate missing rho2
        elif rho2 is None:
            rho2 = (rho1 * a1 * v1) / (a2 * v2)
            print(f"\nOutlet density rho2 = {rho2:.3f} kg/m^3")

        # Calculate missing V1
        elif v1 is None:
            v1 = (rho2 * a2 * v2) / (rho1 * a1)
            print(f"\nInlet velocity V1 = {v1:.3f} m/s")

        # Calculate missing A1
        elif a1 is None:
            a1 = (rho2 * a2 * v2) / (rho1 * v1)
            print(f"\nInlet area A1 = {a1:.3f} m^2")

        # Calculate missing rho1
        elif rho1 is None:
            rho1 = (rho2 * a2 * v2) / (a1 * v1)
            print(f"\nInlet density rho1 = {rho1:.3f} kg/m^3")


# --------------------------------------------------
# INVALID FLOW TYPE
# --------------------------------------------------

else:
    print("\nError: Please enter either 'compressible' or 'incompressible'.")