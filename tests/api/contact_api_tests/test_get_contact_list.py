import requests
import pytest
from utils.api_helper import get_auth_token
from user_data import BASE_URL

@pytest.fixture
def get_token():
    return get_auth_token()

def test_get_contact_list(get_token):
    token = get_token
    
    contact_list_url = f"{BASE_URL}/contacts"
    
    headers = {"Authorization": f"Bearer {token}"}
    contact_list_response = requests.get(contact_list_url, headers=headers)
    
    assert contact_list_response.status_code == 200, f"Request failed with status code {contact_list_response.status_code}: {contact_list_response.text}"