import unittest
import phonebook

class TestPhoneNumberAndEmailAddressValidation(unittest.TestCase):

    def test_valid_phone_number(self):
        self.assertTrue(phonebook.Phonebook().validate_phone_number("(123) 456-7890"), "Should be a valid phone number")

    def test_invalid_phone_number(self):
        self.assertFalse(phonebook.Phonebook().validate_phone_number("1234567890"), "Should be an invalid phone number")

    def test_valid_email_address(self):
        self.assertTrue(phonebook.Phonebook().validate_email_address("rkuma064@uottawa.ca"), "Should be a valid email address")

    def test_invalid_email_address(self):
        self.assertFalse(phonebook.Phonebook().validate_email_address("raviuottawaca"), "Should be an invalid email address")

if __name__ == "__main__":
    unittest.main()

