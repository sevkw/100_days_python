PLACE_HOLDER = "[name]"


with open(r".\Input\Names\invited_names.txt", "r") as names_file:
    names = names_file.readlines()
    print(names)

with open(r".\Input\Letters\starting_letter.txt", "r") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACE_HOLDER, stripped_name)

        with open(f".\Output\ReadyToSend\letter_for_{stripped_name}.txt", "w") as completed_letter:
            completed_letter.write(new_letter)

