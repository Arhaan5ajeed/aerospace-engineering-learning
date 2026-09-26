'''Welcome to the Indian Air Force Fighter Jet Database'''

#--------------------------------------------------------------------------------------------------------------------
# Creating a dictionary to store fighter jet information

fighter_jet_database = [
                        {'name' : "Su-30MKI", 
                        'role' : 'Multirole Air Superiority Fighter' ,
                        'empty_mass_kg' : 18400 ,
                        'max_takeoff_mass_kg' : 38800 ,
                        'length_m' : 21.935 ,
                        'wingspan_m' : 14.7 ,
                        'wing_area_m2' : 62.0 ,
                        'max_speed_mach' : 2.0,
                        'service_ceiling_m' : 17300 ,
                        'engine_count' : 2 },

                        {'name' : "Rafale", 
                        'role' : 'Multirole Fighter' ,
                        'empty_mass_kg' : 10000 ,
                        'max_takeoff_mass_kg' : 24500 ,
                        'length_m' : 15.3 ,
                        'wingspan_m' : 10.9 ,
                        'wing_area_m2' : 45.7 ,
                        'max_speed_mach' : 1.8,
                        'service_ceiling_m' : 15240 ,
                        'engine_count' : 2 },

                        {'name' : "Tejas", 
                        'role' : 'Lightweight Multirole Fighter' ,
                        'empty_mass_kg' : 6560 ,
                        'max_takeoff_mass_kg' : 13500 ,
                        'length_m' : 13.2 ,
                        'wingspan_m' : 8.2 ,
                        'wing_area_m2' : 38.4 ,
                        'max_speed_mach' : 1.6,
                        'service_ceiling_m' : 15240 ,
                        'engine_count' : 1 },

                        {'name' : "MiG-29UPG" ,
                        'role' : 'Multirole Fighter' ,
                        'empty_mass_kg' : 11600 ,
                        'max_takeoff_mass_kg' : 22000,
                        'length_m' : 17.32 ,
                        'wingspan_m' : 11.36 ,
                        'wing_area_m2' : 38.1 ,
                        'max_speed_mach' : 2.25,
                        'service_ceiling_m' : 18000 ,
                        'engine_count' : 2 },
                        
                        {'name' : "Mirage 2000", 
                        'role' : 'Multirole/air-defense fighter' ,
                        'empty_mass_kg' : 7500 ,
                        'max_takeoff_mass_kg' : 17000 ,
                        'length_m' : 14.36 ,
                        'wingspan_m' : 9.13 ,
                        'wing_area_m2' : 41.98 ,
                        'max_speed_mach' : 2.2 ,
                        'service_ceiling_m' : 16460 ,
                        'engine_count' : 1 },

                        {'name' : "Jaguar", 
                        'role' : 'Ground attack aircraft' ,
                        'empty_mass_kg' : 7700 ,
                        'max_takeoff_mass_kg' : 15700 ,
                        'length_m' : 16.8 ,
                        'wingspan_m' : 8.69 ,
                        'wing_area_m2' : 24.0 ,
                        'max_speed_mach' : 1.6,
                        'service_ceiling_m' : 15240 ,
                        'engine_count' : 2 }
                        ]


#------------------------------------------------------------------------------------------
#Creating Menu for user to select fighter jet information
while True:
    print('-' * 80)
    print("============= Welcome to the Indian Air Force Fighter Jet Database =============")
    print('-' * 80)

    print()

    print("1. Display all fighter jets")
    print("2. Search fighter jet by name")
    print("3. Search fighter jets (2) to compare")
    print("4. Calculate wing loading of a fighter jet")
    print("5. Calculate thrust-to-weight ratio of a fighter jet")
    print("6. Display Database")
    print("7. Add more fighter jets to the database")
    print("8. Update fighter jet information in the database")
    print("9. Delete fighter jet information from the database")
    print("10. Exit")

    print()

    user_choice = input("Enter your choice (1-10): ")

    if user_choice == '1':
        print("Displaying all fighter jets in the database:")
        print(1, fighter_jet_database[0]['name'])
        print(2, fighter_jet_database[1]['name'])
        print(3, fighter_jet_database[2]['name'])
        print(4, fighter_jet_database[3]['name'])
        print(5, fighter_jet_database[4]['name'])
        print(6, fighter_jet_database[5]['name'])
    #------------------------------------------------------------------------------------------------------------------------------------
    elif user_choice == '2':
        search_name = input("Enter the name of the fighter jet to search: ").strip()
        found = False
        for jet in fighter_jet_database:
            if jet['name'].lower() == search_name.lower():
                print(f"Fighter Jet Found: {jet['name']}")
                print(f"Role: {jet['role']}")
                print(f"Empty Mass (kg): {jet['empty_mass_kg']}")
                print(f"Max Takeoff Mass (kg): {jet['max_takeoff_mass_kg']}")
                print(f"Length (m): {jet['length_m']}")
                print(f"Wingspan (m): {jet['wingspan_m']}")
                print(f"Wing Area (m^2): {jet['wing_area_m2']}")
                print(f"Max Speed (Mach): {jet['max_speed_mach']}")
                print(f"Service Ceiling (m): {jet['service_ceiling_m']}")
                print(f"Engine Count: {jet['engine_count']}")
                found = True
                break
        if not found:
            print("Fighter Jet not found in the database.")
    #------------------------------------------------------------------------------------------------------------------------------------
    elif user_choice == '3': 
        jet_one = input("Enter the name of First Jet to compare: ").strip()
        jet_two = input("Enter the name of Second Jet to compare: ").strip()

        jet_one = None
        jet_two = None

        for jet in fighter_jet_database:
            if jet['name'].lower() == jet_one.lower():
                jet_one = jet
                break

        for jet in fighter_jet_database:
            if jet['name'].lower() == jet_two.lower():
                jet_two = jet
                break
        if jet_one is None or jet_two is None:
            print("One or both aircrafts are not found.")
        else:
            print()
            print()
            print("=" * 70)
            print(f"{jet_one['name']} vs {jet_two['name']}")
            print("=" * 70)

            print(f"{'Specification':<25}{jet_one['name']:<20}{jet_two['name']:<20}")
            print("-" * 65)

            print(f"{'Role':<25}{jet_one['role']:<20}{jet_two['role']:<20}")
            print(f"{'Empty Mass (kg)':<25}{jet_one['empty_mass_kg']:<20}{jet_two['empty_mass_kg']:<20}")
            print(f"{'MTOW (kg)':<25}{jet_one['max_takeoff_mass_kg']:<20}{jet_two['max_takeoff_mass_kg']:<20}")
            print(f"{'Length (m)':<25}{jet_one['length_m']:<20}{jet_two['length_m']:<20}")
            print(f"{'Wingspan (m)':<25}{jet_one['wingspan_m']:<20}{jet_two['wingspan_m']:<20}")
            print(f"{'Wing Area (m²)':<25}{jet_one['wing_area_m2']:<20}{jet_two['wing_area_m2']:<20}")
            print(f"{'Max Speed (Mach)':<25}{jet_one['max_speed_mach']:<20}{jet_two['max_speed_mach']:<20}")
            print(f"{'Service Ceiling (m)':<25}{jet_one['service_ceiling_m']:<20}{jet_two['service_ceiling_m']:<20}")
            print(f"{'Engine Count':<25}{jet_one['engine_count']:<20}{jet_two['engine_count']:<20}")
    #------------------------------------------------------------------------------------------------------------------------------------
    elif user_choice == '4':
        jet_name = input("Enter the name of the fighter jet to calculate wing loading: ").strip()
        found = False
        for jet in fighter_jet_database:
            if jet['name'].lower() == jet_name.lower():
                weight_N = jet['max_takeoff_mass_kg'] * 9.81 #Force as: F = mg (a=g; g = 9.81)
                wing_loading = weight_N / jet['wing_area_m2']
                print(f"Wing Loading of {jet['name']}: {wing_loading:.2f} N/m²")
                found = True
                break
        if not found:
            print("Fighter Jet not found in the database.")
    #------------------------------------------------------------------------------------------------------------------------------------
    elif user_choice == '5':
        jet_name = input("Enter the name of the fighter jet to calculate thrust-to-weight ratio: ").strip()
        found = False
        for jet in fighter_jet_database:
            if jet['name'].lower() == jet_name.lower():
                # Assuming each engine produces a thrust of 125 kN (this is a simplification)
                thrust_per_engine_kN = 125
                total_thrust_kN = thrust_per_engine_kN * jet['engine_count']
                total_thrust_N = total_thrust_kN * 1000  # Convert kN to N
                weight_N = jet['max_takeoff_mass_kg'] * 9.81  # Weight in Newtons
                thrust_to_weight_ratio = total_thrust_N / weight_N
                print(f"Thrust-to-Weight Ratio of {jet['name']}: {thrust_to_weight_ratio:.2f}")
                found = True
                break
        if not found:
            print("Fighter Jet not found in the database.")
    #------------------------------------------------------------------------------------------------------------------------------------
    elif user_choice == '6':
        print()
        print("Displaying the entire fighter jet database:")
        print()

        print("-" * 97)
        
        print(
            f"{'Name':<15}"
            f"{'Role':<32}"
            f"{'Empty Mass (kg)':<18}"
            f"{'MTOW (kg)':<15}"
            f"{'Length (m)':<12}"
            f"{'Wingspan (m)':<15}"
            f"{'Wing Area (m²)':<16}"
            f"{'Max Speed':<12}"
            f"{'Ceiling (m)':<15}"
            f"{'Engines':<8}"
            )
        
        print("-" * 97)

        for jet in fighter_jet_database:
            print(
                f"{jet['name']:<15}"
                f"{jet['role']:<32}"
                f"{str(jet['empty_mass_kg']):<18}"
                f"{jet['max_takeoff_mass_kg']:<15}"
                f"{jet['length_m']:<12}"
                f"{jet['wingspan_m']:<15}"
                f"{jet['wing_area_m2']:<16}"
                f"{jet['max_speed_mach']:<12}"
                f"{jet['service_ceiling_m']:<15}"
                f"{jet['engine_count']:<8}"
                )        
    #------------------------------------------------------------------------------------------------------------------------------------
    elif user_choice == '7':
        print("\n---- Add Fighter Jet To The Database ---")
        name = input("Enter aircraft name: ").strip()
        role = input("Enter aircraft role: ").strip()
        empty_mass = float(input("Enter empty mass(Kg): ").strip())
        max_takeoff_mass = float(input("Enter maximum takeoff mass(Kg): ").strip())
        length = float(input("Enter length(m): ").strip())
        wingspan = float(input("Enter wingspan(m): ").strip())
        wing_area = float(input("Enter wing area(m^2): ").strip())
        max_speed = float(input("Enter maximum speed(Mach): ").strip())
        service_ceiling = float(input("Enter service ceiling(m): ").strip())
        engine_count = float(input("Enter number of engines: ").strip())

        new_jet = {
            "name": name,
            "role": role,
            "empty_mass_kg": empty_mass,
            "max_takeoff_mass_kg": float(max_takeoff_mass),
            "length_m": float(length),
            "wingspan_m": float(wingspan),
            "wing_area_m2": float(wing_area),
            "max_speed_mach": float(max_speed),
            "service_ceiling_m": float(service_ceiling),
            "engine_count": int(engine_count)
        }

        fighter_jet_database.append(new_jet)

        print(f"{name} has been added successfully.")
    elif user_choice == '8':
        print("\n--- Update Fighter Jet ---")

        search_name = input("Enter the aircraft name to update: ").strip()

        found = False

        for jet in fighter_jet_database:

            if jet["name"].lower() == search_name.lower():

                found = True

                print(f"\n Updating {jet['name']}")
                print("Press Enter if you want to keep the existing value.\n")

                new_role = input(f"Role [{jet['role']}]: ").strip()
                new_empty_mass = input(f"Empty mass [{jet['empty_mass_kg']}]: ").strip()
                new_max_takeoff_mass = input(f"Maximum takeoff mass [{jet['max_takeoff_mass_kg']}]: ").strip()
                new_length = input(f"Length [{jet['length_m']}]: ").strip()
                new_wingspan = input(f"Wingspan [{jet['wingspan_m']}]: ").strip()
                new_wing_area = input(f"Wing area [{jet['wing_area_m2']}]: ").strip()
                new_max_speed = input(f"Maximum speed [{jet['max_speed_mach']}]: ").strip()
                new_service_ceiling = input(f"Service ceiling [{jet['service_ceiling_m']}]: ").strip()
                new_engine_count = input(f"Engine count [{jet['engine_count']}]: ").strip()
                if new_role != "":
                    jet["role"] = new_role
                if new_empty_mass != "":
                    jet["empty_mass_kg"] = float(new_empty_mass)
                if new_max_takeoff_mass != "":
                    jet["max_takeoff_mass_kg"] = float(new_max_takeoff_mass)
                if new_length != "":
                    jet["length_m"] = float(new_length)
                if new_wingspan != "":
                    jet["wingspan_m"] = float(new_wingspan)
                if new_wing_area != "":
                    jet["wing_area_m2"] = float(new_wing_area)
                if new_max_speed != "":
                    jet["max_speed_mach"] = float(new_max_speed)
                if new_service_ceiling != "":
                    jet["service_ceiling_m"] = float(new_service_ceiling)
                if new_engine_count != "":
                    jet["engine_count"] = int(new_engine_count)
                print("\nAircraft information updated successfully.")
                break
        if not found:
            print("Aircraft not found.")
    elif user_choice == '9':
        print("\n--- Delete Fighter Jet ---")

        search_name = input("Enter the aircraft name to delete: ").strip()

        found = False

        for jet in fighter_jet_database:
            if jet["name"].lower() == search_name.lower():

                found = True

                print(f"\nAircraft found: {jet['name']}")

                confirmation = input("Are you sure you want to delete it? (yes/no): ").strip().lower()
                if confirmation == "yes":
                    fighter_jet_database.remove(jet)
                    print(f"{jet['name']} has been deleted successfully.")
                else:
                    print("Deletion cancelled.")
                break
        if not found:
            print("Aircraft not found.")
    elif user_choice == '10':
        print("Exiting database...")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 10.")


