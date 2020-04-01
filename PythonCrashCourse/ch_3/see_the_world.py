places_to_go = ['Macchu Pichu', 'Rio de Janeiro', 'Serengeti', 'Cape Town', 'The Alps']

print(places_to_go)

sorted_list = sorted(places_to_go)
print(f"\nHere is the list sorted! {sorted_list}")

print(f"\nDon't worry, I didn't make the sort permanent! {places_to_go}")

places_to_go.reverse()
print(f"\nHere's the list reveresed: {places_to_go}")

places_to_go.reverse()
print(f"\nPut it in reverse Terry! {places_to_go}")

places_to_go.sort()
print(f"\nHere's the list in alpha order: {places_to_go}")

places_to_go.sort(reverse=True)
print(f"\nHere's the list in reverse alpha order: {places_to_go}")