# ex 10.1
filename = 'learning_python.txt'

print(f"Printing contents of {filename}:")

with open(filename) as file_object:
    contents = file_object.read()
print(contents)    

print(f"\nPrinting {filename} line by line:")

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
        
print(f"\nPrinting {filename} by reading into a list first: ")

with open(filename) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print(line.rstrip())
    
#ex 10.2
print(f"\nNow I will replace Python with Golang:")
with open(filename) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    line = line.replace('Python', 'Golang')
    print(line.rstrip())