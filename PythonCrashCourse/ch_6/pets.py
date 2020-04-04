pet_list = []
pet = {
    'name': 'Bob',
    'type': 'cat',
    'color': 'black',
    'temperament': 'conniving',
    'owner': 'Patty Ike'
}

pet_list.append(pet)

pet = {
    'name': 'Harry',
    'type': 'dog',
    'color': 'tan',
    'temperament': 'energetic',
    'owner': 'Billy Bob'
}

pet_list.append(pet)

pet = {
    'name': 'Chester',
    'type': 'squirrel',
    'color': 'brown',
    'temperament': 'calm',
    'owner': 'Sally Sue'
}

pet_list.append(pet)

for pet in pet_list:
    print(f"\nHere's {pet['name'].title()}'s info:")
    for k,v in pet.items():
        print(f"{k.title()} is {v}")