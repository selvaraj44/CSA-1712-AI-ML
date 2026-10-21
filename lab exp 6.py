location = input("Enter the vacuum cleaner location (A/B): ").upper()
room_a = input("Enter the status of Room A (Clean/Dirty): ").capitalize()
room_b = input("Enter the status of Room B (Clean/Dirty): ").capitalize()

while True:
    if location == "A":
        if room_a == "Dirty":
            print("Action: Suck dirt in Room A")
            room_a = "Clean"
        elif room_b == "Dirty":
            print("Action: Move Right to Room B")
            location = "B"
        else:
            print("Both rooms are clean.")
            break
    else:
        if room_b == "Dirty":
            print("Action: Suck dirt in Room B")
            room_b = "Clean"
        elif room_a == "Dirty":
            print("Action: Move Left to Room A")
            location = "A"
        else:
            print("Both rooms are clean.")
            break

print("Final status:")
print("Room A:", room_a)
print("Room B:", room_b)
