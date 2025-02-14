from playwright.sync_api import Page

class ContactDetailsPage:
    
    def __init__(self, page: Page):
        self.page = page
        self.first_name_locator = self.page.locator("span#firstName")
        self.last_name_locator = self.page.locator("span#lastName")
        
    def click_on_delete_contact_button(self):
        self.page.click("#delete", force=True)
        
    def click_on_edit_contact_button(self):
        self.page.click("#edit-contact", force=True)
        
    def click_on_return_to_contact_list_button(self):
        self.page.click("#return")
        
    def verify_first_name(self, expected_first_name: str):
        self.first_name_locator.wait_for(state="visible", timeout=5000)
        actual_first_name = self.first_name_locator.inner_text().strip()
        assert actual_first_name == expected_first_name, f"Expected first name '{expected_first_name}', but got '{actual_first_name}'"
        
    def verify_last_name(self, expected_last_name: str):
        self.last_name_locator.wait_for(state="visible", timeout=5000)
        actual_last_name = self.last_name_locator.inner_text().strip()
        assert actual_last_name == expected_last_name, f"Expected last name '{expected_last_name}', but got '{actual_last_name}'"