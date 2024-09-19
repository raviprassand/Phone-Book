from model.contact import Contact
from datetime import datetime
import re

import csv

class Phonebook:

    """
    The Phonebook class allows users to create, update, delete, search, and perform various operations on contacts.
    """

    def __init__(self):
        self.contacts = [Contact]*0
        print("Starting phonebook application...")

    def search_contacts(self):

        """
        This function searches for contacts in the contact list based on user-defined criteria.
        """

        choice = input("Options: \n 1. Search with name or phone number \n " +
                       "2. Search for contacts added within specific time frame \n How do you want to search for the contact: ")

        if choice == "1":
            user_input = input("To search for contacts, start entering characters below and press enter to see results: \n")
            counter = 0

            print("Below is a list of matching results: \n")
            for contact in self.contacts:
                if (user_input in contact.get_first_name()
                        or user_input in contact.get_last_name()
                        or user_input in contact.get_phone_number()
                        or user_input in contact.get_email_address()
                        or user_input in contact.get_address()):

                    print("Contact id: ", counter)
                    contact.print_contact()
                    counter+=1
                    print("\n \n")

        elif choice == "2":
            start_date = input("Please enter start date in yyyy/MM/dd format: ")
            end_date = input("Please enter end date in yyyy/MM/dd format: ")
            while True:

                try:
                    start_time=datetime(*[int(i) for i in start_date.split('/')])
                    end_time=datetime(*[int(i) for i in end_date.split('/')]).replace(hour=23,minute=59,second=59)
                    break
                except:
                    print("Please enter a valid date")
            print("Start time: ", start_time)
            print("End Time: ", end_time)
            filtered_contacts = [filtered_contact for filtered_contact in self.contacts if start_time <= filtered_contact.create_time <= end_time]

            print("\nBelow is a list of matching results: \n")
            counter = 0

            for contact in filtered_contacts:
                print("Contact id: ", counter)
                contact.print_contact()
                counter+=1
                print("\n \n")

        else:
            print("Please enter a valid option")

    def create_contact(self):

        """
        This function creates a new contact and adds it to the contact list.
        """

        print("Creating contact...")

        print("Options: \n 1. Enter individual contact manually \n 2. Load contacts in batch from csv file")

        batch_load = input("How do you want to add contact: ")

        if batch_load=="1":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")

            while True:
                phone_number = input("Enter phone number in (XXX) XXX-XXXX format : ")

                if self.validate_phone_number(phone_number)==False:
                    print("Please enter a valid phone number. Make sure format is (XXX) XXX-XXXX")
                    continue
                else:
                    break

            while True:
                email_address = input("Enter email address, press enter to skip: ")
                if email_address=="": email_address=None

                if self.validate_email_address(email_address)==False:
                    print("Please enter a valid email address.")
                    continue
                else:
                    break

            address = input("Enter address: ")
            if address=="": address=None

            contact_exists=False

            for contact in self.contacts:
                if contact.get_first_name()==first_name and contact.get_last_name()==last_name:
                    contact_exists=True

            if contact_exists==True:
                print("Contact already exists! Please check the contact details and delete or update it as per your need.")

            else:
                new_contact = Contact(first_name,last_name,phone_number,email_address,address)
                self.contacts.append(new_contact)
                print("Contact added successfully!")
                self.print_all_contacts()

        elif batch_load=="2":
            print("\n We have sample_contacts.csv file already present in data folder. \n You can copy your required csv file to that path first.")
            file_name = input("Now enter the file name you want to load from the data folder:")
            csv_file_path = "data/"+file_name
            try:
                with open(csv_file_path, mode='r', newline='') as file:
                    csv_reader = csv.reader(file)

                    for contact in csv_reader:

                        first_name = contact[0]
                        last_name = contact[1]

                        phone_number = contact[2]
                        if self.validate_phone_number(phone_number)==False:
                            print("Phone number: ", phone_number, " is not valid format (XXX) XXX-XXXX, exiting csv file. Please try again after fixing the value in csv file.")
                            return

                        email_address = contact[3]
                        if email_address!="" and self.validate_email_address(email_address)==False:
                            print("Email address: ", email_address, " is not valid format, exiting csv file. Please try again after fixing the value in csv file.")
                            return

                        address = contact[4]

                        contact_exists=False

                        for contact in self.contacts:
                            if contact.get_first_name()==first_name and contact.get_last_name()==last_name:
                                contact_exists=True

                        if contact_exists==True:
                            print("Contact with first name: ", first_name, " and last name: ", last_name +
                                  " already exists! Please check the contact details and delete or update it as per your need.")

                        else:
                            new_contact = Contact(first_name,last_name,phone_number,email_address,address)
                            self.contacts.append(new_contact)

                    print("Contacts added successfully from csv file in batch")
                    self.print_all_contacts()
            except:
                print("Error opening the file, please check the file name.")

        else:
            print("Please enter a valid option!")

    def validate_phone_number(self, phone_number):

        """
        This function validates a phone number to ensure it matches the format '(###) ###-####'.

        """

        pattern = r'^\(\d{3}\) \d{3}-\d{4}$'

        if re.match(pattern,phone_number):
            return True
        else:
            return False

    def validate_email_address(self, email_address):

        """
        This function validates an email address to ensure it matches a standard email format.
        """

        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if re.match(pattern, email_address):
            return True
        else:
            return False

    def update_contact(self):

        first_name = input("Enter first name of contact: ")
        last_name = input("Enter last name of contact: ")
        found_contact=False
        for contact in self.contacts:
            if contact.get_first_name()==first_name and contact.get_last_name()==last_name:
                found_contact=True
                print("Fields: \n 1. First Name \n 2. Last Name \n 3. Phone Number \n 4. Email Address \n 5. Address")
                user_input = input("Enter which field you want to update: ")
                if user_input=="1":
                    updated_first_name=input("Enter the new first name: ")
                    contact.update_first_name(updated_first_name)
                elif user_input=="2":
                    updated_last_name=input("Enter the new last name: ")
                    contact.update_last_name(updated_last_name)
                elif user_input=="3":
                    updated_phone_number=input("Enter the new phone number: ")
                    contact.update_phone_number(updated_phone_number)
                elif user_input=="4":
                    updated_email_address=input("Enter the new email address: ")
                    contact.update_email_address(updated_email_address)
                elif user_input=="5":
                    updated_address=input("Enter the new address: ")
                    contact.update_address(updated_address)
                else:
                    print("Please enter a valid option!")
                self.print_all_contacts()

        if found_contact==False:
            print("Contact does not exist, please check and re enter.")

    def delete_contact(self):

        first_name = input("Enter first name of contact to be deleted: ")
        last_name = input("Enter last name of contact to be deleted: ")
        found_contact=False

        for contact in self.contacts:
            if contact.get_first_name()==first_name and contact.get_last_name()==last_name:
                found_contact=True
                self.contacts.remove(contact)
                print("Contact deleted successfully!")

        if found_contact==False:
            print("Contact does not exist, please check and re enter.")

    def print_all_contacts(self):

        counter = 0
        if(self.contacts.count==0):
            print("Contact list is empty, please add new contacts.")
        else:
            print("\nFull Contact List: ")
            for contact in self.contacts:
                print("Contact id: ", counter)
                contact.print_contact()
                counter+=1
                print("\n \n")

    def print_contact_history(self):

        first_name = input("Enter first name of contact: ")
        last_name = input("Enter last name of contact: ")
        found_contact=False
        for contact in self.contacts:
            if contact.get_first_name()==first_name and contact.get_last_name()==last_name:
                found_contact=True
                print("Contact History: ", contact.get_contact_history())

        if found_contact==False:
            print("Contact does not exist, please check the first and last name you entered.")

    def sort_contacts(self):

        choice=input("\n\nOptions: \n1. Ascending \n2. Descending \n\nHow do you want to sort them: ")

        if choice=="1":
            self.contacts.sort(key=lambda contact: contact.get_first_name())
            print("Contacts sorted in ascending order. Press 4 to view all contacts.")
        elif choice=="2":
            self.contacts.sort(key=lambda contact: contact.get_first_name(), reverse=True)
            print("Contacts sorted in descending order. Press 4 to view all contacts.")
        else:
            print("Please enter a valid option")

    def group_contacts(self):


        print("Grouping contacts by initial letter of last name")
        self.contacts.sort(key=lambda contact:contact.get_last_name()[0] )
        print("Contacts successfully grouped. Press 4 to view all contacts.")
