import requests
import pytest
from utils.api_helper import generate_random_contact_data, get_auth_token
from user_data import BASE_URL

@pytest.fixture
def get_token():
    return get_auth_token()

@pytest.fixture
def new_contact_data():
    return generate_random_contact_data()

@pytest.fixture
def create_new_contact(get_token, new_contact_data):
    add_contact_url = f"{BASE_URL}/contacts"
    
    headers = {
        "Authorization": f"Bearer {get_token}"
    }
    
    response = requests.post(add_contact_url, json=new_contact_data, headers=headers)
    
    assert response.status_code == 201, f"Failed to create user: {response.status_code}, {response.text}"
    created_contact = response.json()
    return created_contact

def test_create_and_delete_contact(get_token, create_new_contact):
    created_contact = create_new_contact
        
    contact_id = created_contact["_id"]
    
    delete_contact_url = f"{BASE_URL}/contacts/{contact_id}"
    headers = {
        "Authorization": f"Bearer {get_token}"
    }
    
    delete_response = requests.delete(delete_contact_url, headers=headers)
    assert delete_response.status_code == 200, f"Failed to delete contact: {delete_response.status_code}, {delete_response.text}"
    
    verify_contact_response = requests.get(delete_contact_url, headers=headers)
    assert verify_contact_response.status_code == 404, f"Contact was not deleted successfully. Status Code: {verify_contact_response.status_code}"