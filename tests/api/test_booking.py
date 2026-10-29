import pytest
from api.booking_client import build_booking
from config import ADMIN_USER, ADMIN_PASSWORD


@pytest.mark.smoke
@pytest.mark.api
def test_create_token_success(booking_client):  # TC_API_002
    resp = booking_client.create_token(ADMIN_USER, ADMIN_PASSWORD)

    assert resp.status_code == 200
    body = resp.json()
    assert "token" in body
    assert isinstance(body["token"], str) and body["token"] != ""

@pytest.mark.regression
@pytest.mark.api
def test_create_token_bad_credentials(booking_client):  # TC_API_003
    # TODO: gọi create_token với mật khẩu sai
    resp = booking_client.create_token(ADMIN_USER, "wrong_password")
    assert resp.status_code == 200
    body = resp.json()
    assert "reason" in body
    assert body["reason"] == "Bad credentials"

@pytest.mark.regression
@pytest.mark.api
def test_get_booking_detail(booking_client, new_booking):  # TC_API_006
    booking_id = new_booking["id"]
    payload = new_booking["payload"]

    resp = booking_client.get_booking(booking_id)
    assert resp.status_code == 200
    body = resp.json()
    assert body["firstname"] == payload["firstname"]
    assert body["lastname"] == payload["lastname"]
    assert body["totalprice"] == payload["totalprice"]
    assert body["depositpaid"] == payload["depositpaid"]
    assert body["bookingdates"]["checkin"] == payload["bookingdates"]["checkin"]
    assert body["bookingdates"]["checkout"] == payload["bookingdates"]["checkout"]

@pytest.mark.regression
@pytest.mark.api
def test_get_booking_not_found(booking_client):  # TC_API_007
    resp = booking_client.get_booking(99999)
    assert resp.status_code == 404

@pytest.mark.smoke
@pytest.mark.api
def test_create_booking(booking_client, token):  # TC_API_008
    payload = build_booking()
    resp = booking_client.create_booking(payload)
    assert resp.status_code == 200

@pytest.mark.regression
@pytest.mark.api
def test_update_booking_with_token(booking_client, new_booking, token):  # TC_API_011
    booking_id = new_booking["id"]
    payload = build_booking(firstname="Updated", lastname="User")
    resp = booking_client.update_booking(booking_id, payload, token)
    assert resp.status_code == 200
    body = resp.json()
    assert body["firstname"] == "Updated"
    assert body["lastname"] == "User"

    @pytest.mark.regression
    @pytest.mark.api
    def test_update_booking_without_token(booking_client, new_booking):  # TC_API_012
        booking_id = new_booking["id"]
        payload = build_booking(firstname="Updated", lastname="User")
        resp = booking_client.update_booking(booking_id, payload)
        assert resp.status_code == 403
        body = resp.json()
        assert "reason" in body
        assert body["reason"] == "Forbidden"

@pytest.mark.regression
@pytest.mark.api
def test_delete_booking_with_token(booking_client, new_booking, token):  # TC_API_014
    booking_id = new_booking["id"]
    resp = booking_client.delete_booking(booking_id, token)
    assert resp.status_code == 201