from django.test import Client
import pytest

def test_home_view():
    client = Client()
    response = client.get('/home/')
    assert response.status_code == 200
    assert b'Welcome to the CICD Pipeline app!' in response.content

@pytest.mark.django_db
def test_dashboard_view():
    client = Client()
    response = client.get('/dashboard/')
    assert response.status_code == 200
    assert b'Hello from the Kuldeep Devda Website!' in response.content

