#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("./Input/Letters/starting_letter.txt") as example:
    email = example.read()
    with open("./Input/Names/invited_names.txt") as names:
        for name in names:
            with open(f"./Output/ReadyToSend/{name.rstrip()}.txt",'w') as letter:
                custom_email = email.replace("[name]",name.rstrip())
                letter.write(custom_email)