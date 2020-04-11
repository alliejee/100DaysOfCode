#ex 10.6 & 7
print("Let's add some numbers together!")
print("If you don't want to, feel free to enter 'q' to exit.")

adding = True

while adding:
    first_num = input("Enter 1st number: ")
    if first_num == 'q':
        break
    second_num = input("Enter 2nd number: ")
    if second_num == 'q':
        break
    try:
        answer = int(first_num) + int(second_num)
    except ValueError:
        print("I can only add numbers!")
    else:
        print(answer)    