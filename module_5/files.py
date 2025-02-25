# Working with Files

with open("my_file.txt", "r") as f:
    read_data = f.read()

print(f"File closed: {f.closed}\n")
print(f"File contents:\n{read_data}\n")

# Read a file in chunks
with open("my_file.txt", "r") as f:
    first_line = f.read(11)
    rest_of_file = f.read()

print(f"Read first line: {first_line}\n")
print(f"Read rest of file:{rest_of_file}\n")

# Use a for loop to loop through the lines one at a time
with open("my_file.txt", "r") as f:
    print("One more time in upper case:")
    for line in f:
        print(line.upper(), end='')

with open("my_file.txt", "w") as f:
    f.write("Add something new\n")

with open("my_file.txt", "r") as f:
    print("\nWrite mode overwrites the file:")
    print(f.read())

with open("my_file.txt", "a") as f:
    f.write("Add this to the file")

with open("my_file.txt", "r") as f:
    print("Append mode writes to the end of the file:")
    print(f.read())
