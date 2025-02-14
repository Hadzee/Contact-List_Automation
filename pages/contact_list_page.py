from playwright.sync_api import Page

class ContactListPage:
    
    def __init__(self, page: Page):
        self.page = page
        self.contact_table = self.page.locator("table.contactTable tbody")
        
    def click_on_add_new_contact_button(self):
        self.page.click("#add-contact")
        
    def click_on_logout_button(self):
        self.page.click("#logout")
    
    def is_contact_added(self, contact_name: str) -> bool:
        self.page.wait_for_selector("table.contactTable tr.contactTableBodyRow", timeout=10000)
        contact_rows = self.page.locator("table.contactTable tr.contactTableBodyRow")
        contact_names_in_table = contact_rows.locator("td:nth-child(2)").all_inner_texts()
        return any(name.strip() == contact_name for name in contact_names_in_table)
    
    def is_contact_updated(self, contact_name: str) -> bool:
        self.page.wait_for_selector("table.contactTable tr.contactTableBodyRow", timeout=10000)
        contact_rows = self.page.locator("table.contactTable tr.contactTableBodyRow")
        contact_names_in_table = contact_rows.locator("td:nth-child(2)").all_inner_texts()
        return any(name.strip() == contact_name for name in contact_names_in_table)
    
    def click_on_contact(self, contact_name: str):
        self.page.locator("table.contactTable").wait_for(state="visible", timeout=10000)
        contact_row_locator = self.page.locator(f"tr.contactTableBodyRow >> td:nth-child(2):has-text('{contact_name}')")
        contact_row_locator.wait_for(state="attached", timeout=10000)
        contact_row_locator.click(timeout=10000)