rivers = {
    'nile': 'egypt',
    'mississippi': 'america',
    'euphrates': 'turkey'
    }

for river, location in rivers.items():
    print(f"{river.title()} runs through {location.title()}. ")

print("\n")
    
for river in rivers:
    print(river.title())

print("\n")
    
for location in rivers.values():
    print(location.title())