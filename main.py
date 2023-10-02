Skitarii_Vanguard_Equip=["Archeotech pistol", "Arc rifle", "Plasma caliver", "Radium carbine", "Transuranic arquebus", "Alpha combat weapon ", "Close combat weapon"]
Skitarii_Ranger_Equip=["Archeotech pistol", "Arc rifle", "Galvanic rifle", "Plasma caliver", "Transuranic arquebus", "Alpha combat weapon ", "Close combat weapon"]
Kataphron_Breacher_Equip=["Heavy arc rifle", "Torsion cannon", "Arc claw", "Hydraulic claw"]
Kataphron_Destroyer_Equip=["Cognis flamer", "Heavy grav-cannon", "Kataphron plasma culverin", "Phosphor blaster", "Close combat weapon "]

Admech_Combat_Patrol_Roster=[Skitarii_Vanguard_Equip, Skitarii_Ranger_Equip, Kataphron_Breacher_Equip, Kataphron_Destroyer_Equip]

print("--------------------------------")
print("Manufatorim Requisition Software")
print("---------Version: 0.0.1---------")
print("Omnissiah Bless this sacred code")
print("--------------------------------")

load_view = input("Select Unit: A) Skitarii Vanguard B) Skitarii Ranger C) Kataphron Breacher D) Kataphron Destroyer: ")

if load_view == "A" or load_view == "a":
    print("Printing: Skitarii Vanguard Wargear: " + ", ".join(Skitarii_Vanguard_Equip))
elif load_view == "B" or load_view == "b":
    print("Printing: Skitarii Ranger Wargear: " + ", ".join(Skitarii_Ranger_Equip))
elif load_view == "C" or load_view == "c":
    print("Printing: Kataphron Breacher Wargear: " + ", ".join(Kataphron_Breacher_Equip))
elif load_view == "D" or load_view == "d":
    print("Printing: Kataphron Destroyer Wargear: " + ", ".join(Kataphron_Destroyer_Equip))
else:
    print("ERROR: UNRECOGNIZED COMMAND")
