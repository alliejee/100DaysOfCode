# ex 11.1

def city_country(city, country, population=''):
    location = f"{city.title()}, {country.title()} - population {population}"
    return location

# test = city_country('Chicago','USA', '50000')
# print(test)