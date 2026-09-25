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

print('-' * 80)
print("============= Welcome to the Indian Air Force Fighter Jet Database =============")
print('-' * 80)

print()

print("1. Display all fighter jets")
print("2. Search fighter jet by name")
print("3. Search fighter jets (2) to compare")
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
elif user_choice == '3': 
    jet_one = input("Enter the name of First Jet to compare: ").strip()
    jet_two = input("Enter the name of Second Jet to compare: ").strip()

    jet_1 = None
    jet_2 = None

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

