import pytest
from django.test import Client as DjangoClient
from django.urls import reverse

from client.models import Client
from vehicle.models import Vehicle


@pytest.fixture
def request_browser():
    return DjangoClient()


@pytest.fixture
def db_client():
    return Client.objects.create(email="a@a.com")


@pytest.fixture
def db_vehicle(client):
    return Vehicle.objects.create(client=client, license_plate="AA00AA")


@pytest.mark.django_db
def test_client_create(db_client):
    assert Client.objects.count() == 1


@pytest.mark.django_db
def test_client_update(db_client):
    db_client.email = "b@b.com"
    db_client.save()
    assert Client.objects.count() == 1
    assert Client.objects.first().email == "b@b.com"


@pytest.mark.django_db
def test_client_delete(db_client):
    db_client.delete()
    assert Client.objects.count() == 0


@pytest.mark.django_db
def test_home_view(request_browser):
    response = request_browser.get(reverse("home"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_client_list_view(request_browser, db_client, db_vehicle):
    response = request_browser.get(reverse("client:list_client"))
    assert response.status_code == 200
    assert len(response.context["object_list"]) == 1
    assert response.context["object_list"][0].vehicle_set.count() == 1


@pytest.mark.django_db
def test_client_create_view(request_browser):
    response = request_browser.get(reverse("client:create_client"))
    assert response.status_code == 200
    assert response.context["form"] is not None
    assert response.context.get("object") is None


@pytest.mark.django_db
def test_client_update_view(request_browser, db_client):
    response = request_browser.get(reverse("client:update_client", args=[db_client.pk]))
    assert response.status_code == 200
    assert response.context["form"] is not None
    assert response.context["object"] is not None


@pytest.mark.django_db
def test_client_delete_view(request_browser, db_client):
    response = request_browser.get(reverse("client:delete_client", args=[db_client.pk]))
    assert response.status_code == 200
    assert response.context["object"] is not None
    assert response.context["object"].pk == db_client.pk
