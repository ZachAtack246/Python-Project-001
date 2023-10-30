#Lists for Army Equipment

Skitarii_Vanguard_Equip=["Archeotech pistol", "Arc rifle", "Plasma caliver", "Radium carbine", "Transuranic arquebus", "Alpha combat weapon", "Close combat weapon"]
Skitarii_Ranger_Equip=["Archeotech pistol", "Arc rifle", "Galvanic rifle", "Plasma caliver", "Transuranic arquebus", "Alpha combat weapon", "Close combat weapon"]
Kataphron_Breacher_Equip=["Heavy arc rifle", "Torsion cannon", "Arc claw", "Hydraulic claw"]
Kataphron_Destroyer_Equip=["Cognis flamer", "Heavy grav-cannon", "Kataphron plasma culverin", "Phosphor blaster", "Close combat weapon"]
Tech_Priest_Enginseer_Equip=["Archeotech pistol", "Omnissian axe", "Servo-arm"]
Onager_Dunecrawler_Equip=["Cognis heavy stubber", "Daedalus missile launcher", "Eradication beamer", "Neutron laser", "Icarus array", ]

#Compiles All lists into one Tuple
Admech_Combat_Patrol_Roster=[Skitarii_Vanguard_Equip, Skitarii_Ranger_Equip, Kataphron_Breacher_Equip, Kataphron_Destroyer_Equip]

print("--------------------------------")
print("Manufatorim Requisition Software")
print("---------Version: 0.0.1---------")
print("Omnissiah Bless this sacred code")
print("--------------------------------")

end_set = 0  # Initialize end_set to 0

while True:  # Infinite loop
    load_view = input("Enter load_view (A/B/C/D/E/F/END): ")

    if load_view == "A" or load_view == "a":
        print("Printing: Skitarii Vanguard Wargear: " + ", ".join(Skitarii_Vanguard_Equip))
    elif load_view == "B" or load_view == "b":
        print("Printing: Skitarii Ranger Wargear: " + ", ".join(Skitarii_Ranger_Equip))
    elif load_view == "C" or load_view == "c":
        print("Printing: Kataphron Breacher Wargear: " + ", ".join(Kataphron_Breacher_Equip))
    elif load_view == "D" or load_view == "d":
        print("Printing: Kataphron Destroyer Wargear: " + ", ".join(Kataphron_Destroyer_Equip))
    elif load_view == "E" or load_view == "e":
        print("Printing: Tech Priest Enginseer Wargear: " + ", ".join(Tech_Priest_Enginseer_Equip))
    elif load_view == "F" or load_view == "f":
        print("Printing: Onager_Dunecrawler Wargear: " + ", ".join(Onager_Dunecrawler_Equip))
    elif load_view == "END":
        end_set = 1
        break  # Exit the loop immediately
    else:
        print("ERROR: UNRECOGNIZED COMMAND")