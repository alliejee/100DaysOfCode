#ex 10.8 & 9
file_1 = 'cats.txt'
file_2 = 'dogs.txt'

filenames = [file_1, file_2]

def print_contents(filename):
    with open(filename,'r') as f:
        contents = f.read()
        print(contents)
        
for filename in filenames:
    try:
        print_contents(filename)
        print("\n")
    except FileNotFoundError:
        # print(f"Can't find {filename} ")
        pass
    