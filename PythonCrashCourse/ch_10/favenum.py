# ex 10.11 & 12
import json

try:    
    with open('favenum.txt') as f:
        fave_num = json.load(f)     
except FileNotFoundError:
    fave = input("Hey, what's your fave number? ")
    with open('favenum.txt','w') as f:
        json.dump(fave, f)
else:
    print(f"I know your fave number! It's {fave_num}.")

