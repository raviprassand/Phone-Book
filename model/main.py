import phonebook as pb

def main():

    """
    Main function
    This is the main function where all the phonebook operations are performed based on the options selected which is further accessed to the corresponding classes.
    """

    phonebook = pb.Phonebook()
    while True:

        print("\n\nMain Menu: \n 1. Search Contacts \n 2. Add Contacts \n" +
              " 3. Update Contacts \n 4. Delete Contacts \n 5. View All Contacts \n 6. Print Contact History \n 7. Sort Contacts \n 8. Group contacts \n 9. Exit")
        user_input = input("Please enter your option here: ")

        if user_input == "1":
            phonebook.search_contacts()
        elif user_input == "2":
            phonebook.create_contact()
        elif user_input == "3":
            phonebook.update_contact()
        elif user_input == "4":
            phonebook.delete_contact()
        elif user_input == "5":
            phonebook.print_all_contacts()
        elif user_input == "6":
            phonebook.print_contact_history()
        elif user_input == "7":
            phonebook.sort_contacts()
        elif user_input == "8":
            phonebook.group_contacts()
        elif user_input == "9":
            break
        else:
            print("Please enter a valid option!")

if __name__=="__main__":
    main()
