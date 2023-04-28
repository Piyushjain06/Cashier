import pickle as p


def menu():
    print(
        """\n          M E N U
_____________________________
Choice    --->       Function
--------  --->      ----------
1         --->     Make a bill of a person by Item's serial number
__________________________________________________________________
2         --->     Enter new data into existing data
__________________________________________________________________
3         --->     To Check the Items which are present
__________________________________________________________________
4         --->     change stock of a item 
__________________________________________________________________

5         --->     change price of a item 
__________________________________________________________________
6       --->       Create data
__________________________________________________________________
7         --->     Erase all the presented data
__________________________________________________________________
8         --->     Exit"""
    )


# defining function for file creation
def creation():
    fout = open("file.txt", "wb")
    still = "yes"
    l = []
    while still == "yes" or still == "y":
        item_id = int(input("\nEnter the item id: "))
        print("__________________________________")
        item = input("\nEnter the name: ").lower().strip()
        print("_______________________________________")
        price = int(input(f"\nEnter the price of the {item}: "))
        print("_______________________________________")
        stock = int(input(f"\nEnter stock of the item {item}: "))
        print("_______________________________________")
        l.append([item_id, item, price, stock])
        still = input("\nDo you want to add more elements(Y/N) ").lower()
    p.dump(l, fout)
    fout.close()
    print("____________________________________")


# defining function to add more data into existing data
def appending():
    fin = open("file.txt", "rb")
    read1 = p.load(fin)

    fin.close()
    fout = open("file.txt", "wb")
    still = "yes"
    l = []
    while still == "yes" or still == "y":
        item_id = int(input("\nEnter the item id: "))
        print("__________________________________")
        item = input("\nEnter the name: ").lower().strip()
        print("_______________________________________")
        price = int(input(f"\nEnter the price of the {item}: "))
        print("_______________________________________")
        stock = int(input(f"\nEnter stock of the item {item}: "))
        print("_______________________________________")
        l.append([item_id, item, price, stock])
        still = input("\nDo you want to add more elements(Y/N) ").lower()
    update1 = read1 + l
    p.dump(update1, fout)
    fout.close()
    print("____________________________________")


# defining function to make bill of a person
def billamt():
    fin = open("file.txt", "rb")
    read1 = p.load(fin)
    still = "yes"
    totalamt = 0
    flag = False
    while still == "yes" or still == "y":
        item_id = int(input("\nEnter items's serial number: "))
        stock_used = int(input("\n Enter Quantity: "))
        for i in range(len(read1)):
            if read1[i][0] == item_id:
                flag = True
                if read1[i][3] > 0 and read1[i][3] <= stock_used:
                    amt = (read1[i][2]) * stock_used
                    totalamt = amt + totalamt
                else:
                    print("Item stock is less than the entered amount or is zero")
                still = input("Do you want to add more elements(Y/N) ").lower()
        if flag == False:
            print("____________________________________")
            print(f"Bill id {item_id} is not present !!!")
            print("____________________________________")
    print("____________________________________")
    print(f"\nThe bill total is {totalamt}")
    print("____________________________________")
    fin.close()
    print("_______________________________________")


# defining function to delete all the data from the file
def cleardata1():
    fout = open("file.txt", "wb")
    fout.close()


# defining function to change a item's stock
def changestock():
    fin = open("file.txt", "rb")
    read1 = p.load(fin)
    still = "yes"
    fin.close()
    f1 = open("file.txt", "wb")
    flag = False
    while still == "yes" or still == "y":
        item_id = int(input("\nEnter items's serial number: "))
        stock_changed = int(input("\n Enter Quantity: "))
        for i in range(len(read1)):
            if read1[i][0] == item_id:
                read1[i][3] = stock_changed
                flag = True
        still = input("Do you want to add more elements(Y/N) ").lower()
        if flag == False:
            print("____________________________________")
            print(f"Bill id {item_id} is not present !!!")
            print("____________________________________")
    print("____________________________________")
    p.dump(read1, f1)
    f1.close()


def changeprice():
    fin = open("file.txt", "rb")
    read1 = p.load(fin)
    still = "yes"
    fin.close()
    f1 = open("file.txt", "wb")
    flag = False
    while still == "yes" or still == "y":
        item_id = int(input("\nEnter items's serial number: "))
        price_changed = int(input("\n Enter Quantity: "))
        for i in range(len(read1)):
            if read1[i][0] == item_id:
                read1[i][2] = price_changed
                flag = True
        still = input("Do you want to add more elements(Y/N) ").lower()
        if flag == False:
            print("____________________________________")
            print(f"Bill id {item_id} is not present !!!")
            print("____________________________________")
    print("____________________________________")
    p.dump(read1, f1)
    f1.close()


# defining function to display the data present in the file
def check():
    fin = open("file.txt", "rb")
    read1 = p.load(fin)
    print(read1)
    fin.close()


# main action block
repeat = "y"
while repeat == "yes" or repeat == "y":
    menu()
    choice = int(input("Enter the choice: "))
    if choice == 1:
        billamt()
    if choice == 2:
        appending()
    elif choice == 3:
        check()
    elif choice == 4:
        changestock()
    elif choice == 5:
        changeprice()
    elif choice == 6:
        creation()
    elif choice == 7:
        cleardata1()
    elif choice == 8:
        exit()
    print("_______________________________________")
    repeat = input("Do you want to continue? (Y/N): ").lower()
    print("_______________________________________")
