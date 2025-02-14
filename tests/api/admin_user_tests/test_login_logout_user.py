import requests
from user_data import EMAIL, PASSWORD, BASE_URL

def test_login_and_logout():
    login_url = f"{BASE_URL}/users/login"
    logout_url = f"{BASE_URL}/users/logout"
    
    login_data = {
        "email": EMAIL,
        "password": PASSWORD
    }
    
    login_response = requests.post(login_url, json=login_data)
    
    assert login_response.status_code == 200, f"Login failed with status code {login_response.status_code}: {login_response.text}"
    
    token = login_response.json().get("token")
    assert token, "Token not found in response"
            
    logout_headers = {
        "Authorization": f"Bearer {token}"
    }
    
    logout_response = requests.post(logout_url, headers=logout_headers)
    assert logout_response.status_code == 200, f"Logout failed with status code {logout_response.status_code}: {logout_response.text}"