import requests
import pytest
from utils.api_helper import generate_random_contact_data, get_auth_token
from user_data import BASE_URL

@pytest.fixture
def get_token():
    return get_auth_token()

@pytest.fixture
def create_new_contact(get_token):
    new_contact_data = generate_random_contact_data()
    add_contact_url = f"{BASE_URL}/contacts"
    
    headers = {
        "Authorization": f"Bearer {get_token}"
    }
    
    response = requests.post(add_contact_url, json=new_contact_data, headers=headers)
    assert response.status_code == 201, f"Failed to create contact: {response.status_code}, {response.text}"

    created_contact = response.json()
    return created_contact

def test_get_contact(get_token, create_new_contact):
    created_contact = create_new_contact
    
    contact_id = created_contact["_id"]
    contact_url = f"{BASE_URL}/contacts/{contact_id}"
    
    headers = {"Authorization": f"Bearer {get_token}"}
    contact_response = requests.get(contact_url, headers=headers)
    
    assert contact_response.status_code == 200, f"Request failed with status code {contact_response.status_code}: {contact_response.text}"
    user_profile_data = contact_response.json()
    
    assert user_profile_data["_id"] == contact_id, f"Contact ID does not match: {user_profile_data['_id']} != {contact_id}"
    
    assert user_profile_data["firstName"] == created_contact["firstName"], f"First name does not match: {user_profile_data['firstName']} != {created_contact['firstName']}"
    assert user_profile_data["lastName"] == created_contact["lastName"], f"Last name does not match: {user_profile_data['lastName']} != {created_contact['lastName']}"