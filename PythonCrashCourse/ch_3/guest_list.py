#ex3-4
guest_list = ['Serena', 'Nujabes', 'Anita Baker', 'Maya Angelou']

print(f"{guest_list[0]} you're invited to my place for dinner!")
print(f"{guest_list[1]} you're invited to my place for dinner!")
print(f"{guest_list[2]} you're invited to my place for dinner!")
print(f"{guest_list[3]} you're invited to my place for dinner!")
print("\n")
#ex3-5
print(f"{guest_list[3]} said that they cannot make it.")

guest_list[3] = "Thierry Henry"
print("\n")
print(f"{guest_list[0]} you're invited to my place for dinner!")
print(f"{guest_list[1]} you're invited to my place for dinner!")
print(f"{guest_list[2]} you're invited to my place for dinner!")
print(f"{guest_list[3]} you're invited to my place for dinner!")

#ex3-6
print("\n")
print("The dinner list has grown a bit..")
guest_list.insert(0,"Robert Glasper")
guest_list.insert(3, "Viola Davis")
guest_list.append("Grayson")
print(f"{guest_list[0]} you're invited to my place for dinner!")
print(f"{guest_list[1]} you're invited to my place for dinner!")
print(f"{guest_list[2]} you're invited to my place for dinner!")
print(f"{guest_list[3]} you're invited to my place for dinner!")
print(f"{guest_list[4]} you're invited to my place for dinner!")
print(f"{guest_list[5]} you're invited to my place for dinner!")
print(f"{guest_list[6]} you're invited to my place for dinner!")

#ex3-7
print("\n")
print("Sorry y'all, looks like I couldn't book a bigger table after all...")
print("\n")

guest_6 = guest_list.pop()
guest_5 = guest_list.pop()
guest_4 = guest_list.pop()
guest_3 = guest_list.pop()
guest_2 = guest_list.pop()

print(f"Sorry {guest_6}, you can't come...")
print(f"Sorry {guest_5}, you can't come...")
print(f"Sorry {guest_4}, you can't come...")
print(f"Sorry {guest_3}, you can't come...")
print(f"Sorry {guest_2}, you can't come...")

print(f"{guest_list[1]}, you're still invited!")
print(f"{guest_list[0]}, you're still invited!")

num_guests = len(guest_list)
print(f"\n{num_guests} people are currently invited to the dinner!")
print("\n")
print("Sorry. I changed my mind.. I gotta delete some folks...")

del guest_list[1]
del guest_list[0]

print(guest_list)
