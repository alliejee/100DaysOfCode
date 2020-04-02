current_users = ['the_King', 'the_queen', 'gangsta', 'fluffy1', 'tommycat']

new_users = ['billy_goat', 'lil_betty', 'frank13', 'n00b', 'id3k', 'gangsta']

lower_current_users = [user.lower() for user in current_users] 

print(lower_current_users)        
for user in new_users:
    if user in current_users:
        print(f"Choose another user, {user} is taken.")
    else:
        print(f"{user} is available")