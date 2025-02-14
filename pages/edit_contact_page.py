from playwright.sync_api import Page

class EditContactPage:
    
    def __init__(self, page: Page):
        self.page = page
        
    def fill_first_name(self, first_name: str):
        self.page.fill("#firstName", first_name)
        
    def fill_last_name(self, last_name: str):
        self.page.fill("#lastName", last_name)
        
    def click_on_submit_button(self):
        self.page.click("#submit")