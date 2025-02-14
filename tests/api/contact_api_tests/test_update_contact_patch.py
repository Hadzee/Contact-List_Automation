import requests
import pytest
from utils.api_helper import generate_random_contact_data, generate_random_name, get_auth_token
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

def test_update_contact_name(get_token, create_new_contact):
    created_contact = create_new_contact
    
    updated_name_data = generate_random_name()
    
    contact_id = created_contact["_id"]
    update_url = f"{BASE_URL}/contacts/{contact_id}"
    
    headers = {
        "Authorization": f"Bearer {get_token}"
    }
    
    response = requests.patch(update_url, json=updated_name_data, headers=headers)
    assert response.status_code == 200, f"Failed to update contact: {response.status_code}, {response.text}"
    updated_contact = response.json()
    assert updated_contact['firstName'] == updated_name_data['firstName'], "First name was not updated"