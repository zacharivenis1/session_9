'''journal writing'''

with open("journal.txt","a") as journal:
    while True: #infinite loop until q is pressed
        text = input("Enter your journal entry (press q to quit): ")
        if text == "q":
            break
        journal.write(text.capitalize()+"\n")

