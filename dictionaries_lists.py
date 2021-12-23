contacts = {"name":[], "phone":[]}

while True:
    menu_item = int(input("What do you want? 1-print, 2-add, 3-remove, 4-exit: "))
    if(menu_item == 1):
        print(contacts)
    elif(menu_item ==2):
        print("Adding contact")
    elif(menu_item == 3):
        print("Removing contact")
    elif(menu_item == 4):
        exit()