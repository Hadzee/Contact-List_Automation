import requests
import random
import string
from datetime import datetime, timedelta
from user_data import EMAIL, PASSWORD, BASE_URL

def get_auth_token():
    login_url = f"{BASE_URL}/users/login"
    login_data = {
        "email": EMAIL,
        "password": PASSWORD
    }
    login_response = requests.post(login_url, json=login_data)
    if login_response.status_code != 200:
        raise ValueError(f"Login failed with status code {login_response.status_code}: {login_response.text}")
    
    token = login_response.json().get("token")
    if not token:
        raise ValueError("Token not found in response")
    
    return token

def get_contacts_from_api(token):
    url = f"{BASE_URL}/contacts/"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}")
    
def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def generate_random_email():
    random_string = generate_random_string()
    return f"{random_string}@gmail.com"

def generate_random_birthdate():
    start_date = datetime.now() - timedelta(days=70*365)
    end_date = datetime.now() - timedelta(days=18*365)
    delta_days = (end_date - start_date).days
    random_days = random.randint(0, delta_days)
    random_birthdate = start_date + timedelta(days=random_days)

    return random_birthdate.strftime('%Y-%m-%d')

def generate_random_phone_number():
    area_code = "800"
    central_office_code = random.randint(100, 999)
    subscriber_number = random.randint(1000, 9999)
    phone_number = f"({area_code}) {central_office_code}-{subscriber_number}"
    
    return phone_number

def generate_random_state_province():
    states_provinces = [
        "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
        "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
        "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
    ]
    state_province = random.choice(states_provinces)
    
    return state_province

def generate_random_postal_code():
    postal_code = str(random.randint(10000, 99999))
    return postal_code

def generate_random_name():
    return {
        "firstName": generate_random_string(8).capitalize(),
    }

def generate_random_user_data():
    return {
        "firstName": generate_random_string(8).capitalize(),
        "lastName": generate_random_string(8).capitalize(),
        "email": generate_random_email(),
        "password": generate_random_string(12)
    }
    
def generate_random_contact_data():
    return {
        "firstName": generate_random_string(8).capitalize(),
        "lastName": generate_random_string(8).capitalize(),
        "birthdate": generate_random_birthdate(),
        "email": generate_random_email(),
        "phone": generate_random_phone_number(),
        "street1": generate_random_string(8),
        "street2": generate_random_string(8),
        "city": generate_random_string(8),
        "stateProvince": generate_random_state_province(),
        "postalCode": generate_random_postal_code(),
        "country": generate_random_string(5)
        }