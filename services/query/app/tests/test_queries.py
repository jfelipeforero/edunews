from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

# Test for /create endpoint
def test_create_query():
    payload = {
        "body": {
            "name": "Test Query",
            "description": "This is a test query",
            "username": "test_user",
            "save": "true"
        },
        "country_code": "US",
        "indicator_name": "GDP",
        "year": "2022"
    }
    response = client.post("/create", json=payload)
    assert response.status_code == 200
    assert "data" in response.json()

# Test for /all-queries endpoint
def test_get_all_queries():
    response = client.get("/all-queries")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test for /id/comments endpoint
def test_get_multi():
    params = {
        "country_code": ["US", "CA"],
        "indicator": "GDP",
        "year": "2022"
    }
    response = client.get("/id/comments", params=params)
    assert response.status_code == 200
    assert "data" in response.json()

# Test for /all-indicators endpoint
def test_list_all_indicators():
    response = client.get("/all-indicators")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test for / endpoint
def test_get_by_username():
    params = {"username": "test_user"}
    response = client.get("/", params=params)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test for /all-countries endpoint
def test_list_all_countries():
    response = client.get("/all-countries")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test for /all-queries endpoint (duplicate name, consider changing one of them)
def test_list_queries():
    response = client.get("/all-queries")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test for /{id} endpoint (replace {id} with an actual query ID)
def test_get_by_id():
    query_id = 1  # Replace with an actual query ID
    response = client.get(f"/{query_id}")
    assert response.status_code == 200
    assert "query" in response.json()

