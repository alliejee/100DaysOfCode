# ex 8.12
def sandwichmaker(*ingredients):
    print("Here are the ingredients for your sandwich:")
    for ingredient in ingredients:
        print(ingredient)
    print("\n")
sandwichmaker('tomatos','mayo','pickles')
sandwichmaker('peanut butter', 'jelly')
sandwichmaker('air')