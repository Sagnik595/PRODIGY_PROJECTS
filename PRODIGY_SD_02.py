#contact management system
import os

print("                                     WELCOME TO CONTACT MANAGEMENT SYSTEM")

c = {}
while (1):
    print("1.Add New Contact")
    print("2.Edit Existing Contact")
    print("3.Delete Contact")
    print("4.View Contact List")
    print("5.Terminate")
    ch=int(input("Enter your choice:-"))

    match(ch):
        case 1:
            n = input("Enter Contact Name:-")
            p = input("Enter Phone:-")
            e = input("Enter E-Mail:-")
            c[n] = {"Phone": p, "Email": e}

            print("\n")


        case 2:
            n1=input("Enter the contact name which you want to edit:-")
            print("1.Edit Name")
            print("2.Edit Phone Number")
            print("3.Edit Email")
            ch1=int(input("Enter your choice:-"))
            if ch1 == 1:
                n2 = input("Enter new name: ")
                c[n1]["Name"] = n2
            elif ch1 == 2:
                p1 = input("Enter new phone: ")
                c[n1]["Phone"] = p1
            else:
                e1 = input("Enter new Email: ")
                c[n1]["Email"] = e1

            print("List Updated")

            print("\n")


        case 3:
            k=input("Enter Contact to be deleted:-")
            if (k in c):
                del c[k]
                print("The specified contact has been deleted")
            else:
                print("The specified contact is not present in the contact list!!!")

            print("\n")

        case 4:
            with open("sample.txt", "w") as file:
                for contact, details in c.items():
                    file.write(f"{contact}: {details}\n")
            print("Opening Contact List...")
            os.startfile("sample.txt")

            print("\n")



    if (ch==5):
        print("Thank You for visiting...")
        break


