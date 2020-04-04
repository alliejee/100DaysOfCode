#ex 6.7
people = []

person = {
    'first': 'Brian',
    'last': 'Dawkins',
    'team': 'Eagles',
    'city': 'Philadelphia'
    }

people.append(person)

person = {
    'first': 'Serena',
    'last': 'Williams',
    'team': 'USA',
    'city': 'Compton'
    }

people.append(person)

person = {
    'first': 'Didier',
    'last': 'Drogba',
    'team': 'Chelsea FC',
    'city': 'London'
    }

people.append(person)

for person in people:
    print(f"\n{person}")

