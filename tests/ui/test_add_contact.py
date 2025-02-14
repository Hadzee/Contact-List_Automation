from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.contact_list_page import ContactListPage
from pages.add_contact_page import AddContactPage
from user_data import EMAIL, PASSWORD

def test_add_contact():
     with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        login_page = LoginPage(page)
        login_page.goto()
        login_page.fill_email(EMAIL)
        login_page.fill_password(PASSWORD)
        login_page.click_on_submit_button()
        
        contact_list_page = ContactListPage(page)
        contact_list_page.click_on_add_new_contact_button()
        
        add_contact_page = AddContactPage(page)

        first_name = add_contact_page.generate_random_name(length=6)
        last_name = add_contact_page.generate_random_name(length=8)
        contact_name = f"{first_name} {last_name}"
        
        add_contact_page.fill_first_name(first_name)
        add_contact_page.fill_last_name(last_name)
        add_contact_page.fill_date_of_birth("1998-08-12")
        add_contact_page.fill_email(EMAIL)
        add_contact_page.fill_phone_number("198504839456")
        add_contact_page.fill_address_one("test address 1")
        add_contact_page.fill_address_two("test address 2")
        add_contact_page.fill_city_name("Tuzla")
        add_contact_page.fill_state_province("Tuzlanski Kanton")
        add_contact_page.fill_postal_code("abc1234")
        add_contact_page.fill_country_name("Bosnia and Herzegovina")
        add_contact_page.click_on_submit_button()
        page.wait_for_selector(f"td:has-text('{contact_name}')", timeout=10000)
        
        assert contact_list_page.is_contact_added(contact_name), f"Contact '{contact_name}' was not found in the table!"   
        contact_list_page.click_on_logout_button()
        assert page.inner_text('h1') == "Contact List App", "Did not log out properly."
        
        browser.close()