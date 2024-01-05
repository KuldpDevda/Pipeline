from django.test import Costomer
import pytest


def test_home_view():
    costomer = Costomer()
    response = client.get('/cicd_home/')
    assert response.status_code == 200
    assert b'Welcome to the CICD app!' in response.content

