from playwright.sync_api import Page
import re
import random
import string

class AddContactPage:
    
    def __init__(self, page: Page):
        self.page = page
        self.contact_table = self.page.locator("#myTable tbody")

        
    def fill_first_name(self, first_name: str):
        self.page.fill("#firstName", first_name)
        
    def fill_last_name(self, last_name: str):
        self.page.fill("#lastName", last_name)
    
    def fill_address_one(self, address_one: str):
        self.page.fill("#street1", address_one)
        
    def fill_address_two(self, address_one: str):
        self.page.fill("#street2", address_one)
        
    def fill_city_name(self, city: str):
        self.page.fill("#city", city)
        
    def fill_state_province(self, state: str):
        self.page.fill("#stateProvince", state)
    
    def fill_country_name(self, country: str):
        self.page.fill("#country", country)
        
    def click_on_submit_button(self):
        self.page.click("#submit")
        
    def generate_random_name(self, length=6):
        return ''.join(random.choices(string.ascii_letters, k=length))
    
    def fill_date_of_birth(self, dob: str):
        if not re.match(r"\d{4}-\d{2}-\d{2}", dob):
            raise ValueError("Date must be in the format YYYY-MM-DD.")
        self.page.fill("#birthdate", dob)
        
    def fill_email(self, email: str):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Email must be in the format example@email.com.")
        self.page.fill("#email", email)
        
    def fill_phone_number(self, phone_number: str):
        if not re.match(r"^\d{1,12}$", phone_number):
            raise ValueError("Phone number must contain only digits and be no longer than 15 characters.")
        self.page.fill("#phone", phone_number)
        
    def fill_postal_code(self, postal_code: str):
        if not re.match(r"^[A-Za-z]{3}\d{4}$", postal_code) and not re.match(r"^\d{7}$", postal_code):
            raise ValueError("Postal code must be either 3 letters followed by 4 digits, or exactly 7 digits.")
        self.page.fill("#postalCode", postal_code)