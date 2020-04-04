cities = {
    'Austin': {
        'name': 'Austin',
        'state': 'Texas',
        'population': '90000',
        'fact': 'Austin aint THAT weird'
        },
    'DC': {
        'name': "District of Columbia",
        'state': 'Maryland',
        'population': '650000',
        'fact': 'Capital of the US'
        },
    'New Orleans': {
        'name': "New Orleans",
        'state': 'Louisiana',
        'population': '400000',
        'fact': 'Birthplace of music'
    }
}

for city, city_info in cities.items():
        state = city_info['state']
        population = city_info['population']
        fact = city_info['fact']
        print(f"\nHere are facts about {city}:")
        print(f"{city.title()} is located in is {state}")
        print(f"The population is {population}")
        print(f"A random fact about {city.title()} is that it is -> {fact}")