import requests
import pytest
from utils.api_helper import get_auth_token
from user_data import BASE_URL


@pytest.fixture
def get_token():
    return get_auth_token()

def test_get_user_profile(get_token):
    token = get_token
    
    user_profile_url = f"{BASE_URL}/users/me"
    
    headers = {"Authorization": f"Bearer {token}"}
    user_profile_response = requests.get(user_profile_url, headers=headers)
    
    assert user_profile_response.status_code == 200, f"Request failed with status code {user_profile_response.status_code}: {user_profile_response.text}"