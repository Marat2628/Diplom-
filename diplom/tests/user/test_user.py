from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK
import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_create_user(api_client):
    """Тест создания пользователя"""
    url = reverse('backend:user-register')
    user = {"first_name": "Ivan",
            "last_name": "Petrov",
            "email": "example@example.ru",
            "password": "#321ip321",
            "company": "ikea",
            "position": ""
            }
    resp = api_client.post(url, user)
    assert resp.status_code == HTTP_201_CREATED
    resp_json = resp.json()
    assert resp_json['Status'] == True


