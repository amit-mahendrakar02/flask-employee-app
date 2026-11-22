# Test app 

# Import the necessary modules for testing
import sys
from pathlib import Path 

# Add the parent directory of the current file to the system path to allow importing the app module
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import app  # Import the app module to be tested

# Define a test function to check the home route of the app
def test_home():
    # Create a test client for the app
    client = app.test_client()

    # Send a GET request to the home route
    response = client.get('/')

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

   


# Test the health route of the app
def test_health():
    # Create a test client for the app
    client = app.test_client()

    # Send a GET request to the health route
    response = client.get('/health')

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    data = response.get_json()  # Get the JSON data from the response

    # Assert that the response data contains the expected content
    assert data['status'] == 'UP'


# test the employees route of the app
def test_get_employees():
    # Create a test client for the app
    client = app.test_client()

    # Send a GET request to the employees route
    response = client.get('/api/employees')

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the response data contains at least one employee
    assert len(response.get_json()) == 4  # Assert that the response data contains exactly 4 employees


# Test the employee route of the app with a specific ID
def test_get_employee_by_id():
    # Create a test client for the app
    client = app.test_client()

    # Send a GET request to the employee route with a specific ID
    response = client.get('/api/employees/1')

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the response data contains the expected employee name
    assert response.get_json()["name"] == "Amit"


# Test the employee route of the app with a non-existent ID
def test_employee_not_found():
    # Create a test client for the app
    client = app.test_client()

    # Send a GET request to the employee route with a non-existent ID
    response = client.get('/api/employees/999')

    # Assert that the response status code is 404 (Not Found)
    assert response.status_code == 404

    # Assert that the response data contains the expected error message
    assert response.get_json()["error"] == "Employee not found"
