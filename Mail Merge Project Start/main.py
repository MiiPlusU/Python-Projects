place_holder = "[name]"
names = []

with open("/Users/Ish/Desktop/Python-Projects/Mail Merge Project Start/Input/Names/invited_names.txt", mode = "r") as names_file:
    names_list=names_file.readlines()


with open("/Users/Ish/Desktop/Python-Projects/Mail Merge Project Start/Input/Letters/starting_letter.txt", mode = "r") as letters_file:
    content = letters_file.read()
    for name in names_list:
        strip_name =name.strip()
        new_file= content.replace(place_holder, strip_name)
        with open(f"Output/ReadyToSend/Letter_for_{strip_name}", mode = "w") as final_file:
            final_file.write(new_file)

