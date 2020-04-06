responses = {}

polling = True
while polling:
    name = input("\nWhat's your name? ")
    vacation = input("\nIf you could visit any place in the world, where would you go? ")

    responses[name] = vacation
    
    repeat = input("Would you like another person to answer? (yes/no) ")
    if repeat == 'no':
        polling = False
    
print("\n--Vacation Survey Result--")

for name, vacation in responses.items():
    print(f"{name} wants to go to {vacation}!")