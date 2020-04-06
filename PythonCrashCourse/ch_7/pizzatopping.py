prompt = ("\nPlease enter what toppings you want on your pizza.")
prompt += "\n(Enter 'quit' when you are finished) "

while True:
    topping = input(prompt)
    
    if topping == 'quit':
        print("\n Thanks for your business! Bye!! ")
        break
    else:
        print(f"{topping.title()} has been added!")