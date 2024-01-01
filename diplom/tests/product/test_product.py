from rest_framework.status import HTTP_200_OK
import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_get_category(category_factory, api_client):
    """Тест на получение категории товаров"""
    category1 = category_factory()
    category2 = category_factory()
    url = reverse('backend:categories')
    resp = api_client.get(url)
    resp_json = resp.json()
    assert resp.status_code == HTTP_200_OK
    assert resp_json['count'] == 2

