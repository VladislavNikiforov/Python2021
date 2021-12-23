contacts = {"name":[],"number:":[]}
contacts["name"] = ["Anna", "Artyom", "Vlad", "Denis"]
contacts["number"] = ["+37122333904", "+37129718241", "+37125679316", "+37123744490"]

while True:
    menu = int(input("Choose one variant: 1 - add, 2 - delete, 3 - print, 4 - exit "))
    if (menu == 1):
        print("Adding a contact")
        name = (input("Write name: "))
        number = (input("Write phone number: "))
        contacts["name"].append(name)
        contacts["number"].append(number)
    if (menu == 2):
        print("Delet a contact")
        name = (input("Write name: "))
        index = contacts["name"].index(name)
        contacts["name"].pop(index)
    if (menu == 3):
        print(contacts)
    if (menu == 4):
        exit()