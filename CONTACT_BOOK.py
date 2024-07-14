contact ={}
def display_contact():
    print("Name\t\tContact Number\t\temail\t\taddress")
    for key in contact:
        print("{}\t\t{}\t\t{}\t\t{}".format(key, contact[key][0], contact[key][1], contact[key][2]))
while 'true':
    choice =int(input("1: Add contact\n 2: View contact\n 3: Search contact\n 4:Update contact\n 5: Delete contact\n 6: Exit\n Enter your choice :"))
    if choice ==1:
        name=input("Enter your name :")
        phone=input("Enter the number :")
        email=input("Enter you email :")
        address=input("Enter your adress :")

        contact[name] = (phone, email, address)
        print("Contact added successfully.")
    elif choice==2:
         if not contact:
             print("Empty contact book")
         else:
             display_contact()
    elif choice==3:
          search_name = input("Enter the name to search: ")
          if search_name in contact:
                print("Contact details for {}: ".format(search_name))
                print("Phone Number:", contact[search_name][0])
                print("Email:", contact[search_name][1])
                print("Address:", contact[search_name][2])
          else:
                print("Name '{}' not found in the contact book.".format(search_name)) 
    elif choice==4:
        edit_contact= input("Enter the contact to be edited :")
        if edit_contact in contact:
         phone =input("Enter mobile number")
         email = input("Enter new email: ")
         address = input("Enter new address: ")
         contact[edit_contact]=(phone,email,address)
         print("Contact updated")
         display_contact()
        else:
            print("Name is not found in the contact book ")
    elif choice==5:
       del_contact=input("Enter the contact you want to delete :")
       if del_contact in contact:
           confirm=input("Do you want to delete this contact : ") 
       if confirm == 'y' or confirm =='y':
           contact.pop(del_contact)
           display_contact()
       else:
           print("Name is not found in contact book ")
    else:
        break    