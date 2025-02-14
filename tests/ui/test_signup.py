from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.sign_up_page import SignupPage
from pages.contact_list_page import ContactListPage

def test_signup():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        login_page = LoginPage(page)
        login_page.goto()
        login_page.click_on_sign_up_button()
        
        signup_page = SignupPage(page)
        generated_first_name = signup_page.generate_random_name()
        generated_last_name = signup_page.generate_random_name()
        generated_email = signup_page.generate_random_email()
        generated_password = signup_page.generate_random_password()
        
        signup_page.fill_first_name(generated_first_name)
        signup_page.fill_last_name(generated_last_name)
        signup_page.fill_email()
        signup_page.fill_password()
        signup_page.click_on_submit_button()
        
        login_page.fill_email(generated_email)
        login_page.fill_password(generated_password)
        login_page.click_on_submit_button()
        
        contact_list_page = ContactListPage(page)
        contact_list_page.click_on_logout_button()
        assert page.inner_text('h1') == "Contact List App", "Did not log out properly."
        
        browser.close()