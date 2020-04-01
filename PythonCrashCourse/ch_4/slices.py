pizza_list = ['pepperoni', 'cheese', 'supreme', 'sausage', 'thin crust']

#ex 4.10
print("The first three items in this list are:")
for pizza in pizza_list[0:3]:
    print(pizza)

print("\nThree items from the middle of the list are:")
for pizza in pizza_list[1:4]:
    print(pizza)
    
print("\nThe last three items in the list are:")
for pizza in pizza_list[-3:]:
    print(pizza)

friend_pizzas = pizza_list[:]

#ex 4.11
pizza_list.append("meat lovers")
friend_pizzas.append("cheese crust")

print("\nMy favorite pizzas are:")
for pizza in pizza_list:
    print(pizza)    

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)  
print("I absolutely love pizza!")