file = open("my_file.txt")
contents = file.read() #returns contents as a string
print(contents)
file.close() #to free up resources/memory manually on your pc so the pc doesn't have to

with  open("my_file.txt") as file:
    contents = file.read() #returns contents as a string
    print(contents)

# with keyword will automatically close file when done

with  open("my_file.txt", mode="w") as file:
    file.write("New text.")