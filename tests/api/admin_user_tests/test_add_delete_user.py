import requests
import pytest
from utils.api_helper import generate_random_user_data, get_auth_token
from user_data import BASE_URL

@pytest.fixture
def get_token():
    return get_auth_token()  

@pytest.fixture
def new_user_data():
    return generate_random_user_data()

@pytest.fixture
def create_user(get_token, new_user_data):

    add_user_url = f"{BASE_URL}/users"
    
    headers = {
        "Authorization": f"Bearer {get_token}"
    }
    
    response = requests.post(add_user_url, json=new_user_data, headers=headers)
    assert response.status_code == 201, f"Failed to create user: {response.status_code}, {response.text}"
    created_user = response.json()
    assert 'email' in created_user['user'], f"Expected 'email' key, but got: {created_user}"
    
    return created_user

@pytest.fixture
def get_new_user_token(create_user, new_user_data):

    new_user_email = create_user["user"]["email"]
    new_user_password = new_user_data["password"]
    
    login_url = f"{BASE_URL}/users/login"
    login_data = {
        "email": new_user_email,
        "password": new_user_password
    }
    
    login_response = requests.post(login_url, json=login_data)
    assert login_response.status_code == 200, f"Login failed with status code {login_response.status_code}: {login_response.text}"

    token = login_response.json().get("token")
    assert token, "Token not found in response"
    
    return token

def test_delete_user(get_new_user_token):
    delete_user_url = f"{BASE_URL}/users/me"
    
    headers = {"Authorization": f"Bearer {get_new_user_token}"}
    user_profile_response = requests.delete(delete_user_url, headers=headers)
    
    assert user_profile_response.status_code == 200, f"Request failed with status code {user_profile_response.status_code}: {user_profile_response.text}"
    
    try:
        user_profile_data = user_profile_response.json()
        print(f"User Profile: {user_profile_data}")
    except ValueError:
        print("User profile has been successfully deleted, no further data available.")
        
    user_profile_response_after_deletion = requests.get(delete_user_url, headers=headers)
    assert user_profile_response_after_deletion.status_code == 401, f"User still exists: {user_profile_response_after_deletion.status_code}"