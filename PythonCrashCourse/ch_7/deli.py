sandwich_order = ['grilled cheese', 'ham and cheese', 'sausage', 'pastrami', 'pastrami', 'pastrami']

finished_sandwiches = []

# no pastrami loop ex7.9
print("We are out of pastrami.. Sorry!")
while 'pastrami' in sandwich_order:
    sandwich_order.remove('pastrami')

while sandwich_order:
    sandwich = sandwich_order.pop()
    print(f"I made your {sandwich} sandwich!")
    finished_sandwiches.append(sandwich)

print("\nHere's all the sandwiches I made:")    

for sandwich in finished_sandwiches:
    print(sandwich.title())