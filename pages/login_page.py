from playwright.sync_api import Page

class LoginPage:
    
    def __init__(self, page: Page):
        self.page = page
        
    def goto(self):
       self.page.goto("https://thinking-tester-contact-list.herokuapp.com/")
       
    def fill_email(self, email: str):
        self.page.fill("#email", email)
    
    def fill_password(self, password: str):
        self.page.fill("#password", password) 
        
    def click_on_submit_button(self):
        self.page.click("#submit")
        
    def click_on_sign_up_button(self):
        self.page.click("#signup")  