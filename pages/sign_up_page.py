from playwright.sync_api import Page
import random
import string

class SignupPage:
    
    def __init__(self, page: Page):
        self.page = page
        
    def click_on_submit_button(self):
        self.page.click("#submit")
        
    def click_on_cancel_button(self):
        self.page.click("#cancel")
        
    def generate_random_name(self):
        name_length = random.randint(5, 10)
        random_name = ''.join(random.choices(string.ascii_lowercase, k=name_length)).capitalize()
        return random_name
        
    def generate_random_email(self):
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        email = f"{random_string}@example.com"
        return email
    
    def generate_random_password(self, length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choices(characters, k=length))
        return password
    
    def fill_first_name(self, first_name: str = None):
        first_name = first_name or self.generate_random_name()
        self.page.fill("#firstName", first_name)

    def fill_last_name(self, last_name: str = None):
        last_name = last_name or self.generate_random_name()
        self.page.fill("#lastName", last_name)

    def fill_email(self, email: str = None):
        email = email or self.generate_random_email()
        self.page.fill("#email", email)
        
    def fill_password(self, password: str = None):
        password = password or self.generate_random_password()
        self.page.fill("#password", password)