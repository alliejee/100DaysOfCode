# ex 9.1

class Restaurant:
    """Class to create a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print(f"{self.restaurant_name}")
        print(f"{self.cuisine_type}")
        print(f"The number of customers served: {self.number_served}")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open for business!\n")
    
    def set_number_served(self, num_patrons):
        self.number_served = num_patrons
        
    def increment_number_served(self, new_patrons):
        self.number_served += new_patrons

# class IceCreamStand(Restaurant):
#     """Ice cream stand class that inherits from Restaurant"""
#     def __init__(self, restaurant_name, cuisine_type):
#         """Init attributes of parent class"""
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = []
    
#     def add_flavors(self, new_flavors):
#         self.flavors = new_flavors.items()
    
#     def display_flavors(self):
#         print(f"These are the flavors we have: ")
#         for flavor in self.flavors:
#             print(flavor)
        
# my_stand = IceCreamStand('Frosties', 'ice cream')
# my_stand.flavors = ['strawberry', 'neo', 'sprite']
# print(my_stand.display_flavors())
        

# new_restaurant = Restaurant('Fazolis','Italian')
# new_restaurant.describe_restaurant()
# new_restaurant.open_restaurant()
# new_restaurant.set_number_served(6)
# new_restaurant.describe_restaurant()

# new1_restaurant = Restaurant('Jinya','Japanese')
# new1_restaurant.increment_number_served(7)
# new1_restaurant.describe_restaurant()
# new1_restaurant.open_restaurant()


# new2_restaurant = Restaurant('Rustys','BBQ')
# new2_restaurant.describe_restaurant()
# new2_restaurant.open_restaurant()
