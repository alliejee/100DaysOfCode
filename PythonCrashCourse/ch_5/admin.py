usernames = ['porgy', 'chester', 'lemming', 'botsy','wiley', 'admin']

# usernames = []

if usernames:
    for user in usernames:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?\n")
        else:
            print(f"Hello {user}, thank you for logging in again.\n")
else:
    print("We need to find some users!")

