filename = 'guest_list.txt'

polling = True

while polling:
    guest_name = input("Hello there! Whats youre name? || If you dont want to answer enter 'q' ")

    if guest_name == 'q':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(f"{guest_name} \n")