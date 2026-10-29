import requests
from config import API_URL


def build_booking(**overrides) -> dict:
    """Tạo dữ liệu booking mẫu. Truyền vào trường nào thì ghi đè trường đó."""
    data = {
        "firstname": "Linh",
        "lastname": "Tran",
        "totalprice": 500,
        "depositpaid": True,
        "bookingdates": {"checkin": "2026-11-01", "checkout": "2026-11-05"},
        "additionalneeds": "Breakfast",
    }
    data.update(overrides)
    return data


class BookingClient:
    def __init__(self, base_url: str = API_URL):
        self.base_url = base_url
        self.timeout = 30
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json",
        })

    def create_token(self, username: str, password: str):
        return self.session.post(
            f"{self.base_url}/auth",
            json={"username": username, "password": password},
            timeout=self.timeout,
        )

    def create_booking(self, payload: dict):
        return self.session.post(
            f"{self.base_url}/booking", json=payload, timeout=self.timeout
        )

    def get_booking(self, booking_id):
        return self.session.get(
            f"{self.base_url}/booking/{booking_id}", timeout=self.timeout
        )

    def update_booking(self, booking_id, payload: dict, token: str | None = None):
        headers = {"Cookie": f"token={token}"} if token else {}
        return self.session.put(
            f"{self.base_url}/booking/{booking_id}",
            json=payload, headers=headers, timeout=self.timeout,
        )

    def delete_booking(self, booking_id, token: str | None = None):
        headers = {"Cookie": f"token={token}"} if token else {}
        return self.session.delete(
            f"{self.base_url}/booking/{booking_id}",
            headers=headers, timeout=self.timeout,
        )