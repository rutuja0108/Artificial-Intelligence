# 1. Automatic Light Agent
person = input("Is a person present? (yes/no): ").lower()
daylight = input("Is there daylight? (yes/no): ").lower()

if person == "yes" and daylight == "no":
    print("Light ON")
else:
    print("Light OFF")
  
# 2. Automatic Fan Agent
person = input("Is a person present? (yes/no): ").lower()
temperature = float(input("Enter temperature: "))

if person == "yes" and temperature > 30:
    print("Fan ON")
else:
    print("Fan OFF")

# 3. Vacuum Cleaner Agent
room = input("Is the room dirty? (yes/no): ").lower()

if room == "yes":
    print("Vacuum Cleaner ON")
else:
    print("Room is clean")
