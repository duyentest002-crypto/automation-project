# Automation Testing Project: SauceDemo + Restful Booker

![Tests](https://github.com/<ten-ban>/automation-project/actions/workflows/tests.yml/badge.svg)

Bộ test automation (UI + API) được xây dựng từ bộ test case manual, theo quy trình:
viết test case → chọn case đáng automate → dựng framework → chạy tự động trên CI.

## Công nghệ

Python · Pytest · Playwright · Requests · pytest-html · GitHub Actions

## Phạm vi

| Hệ thống | Loại | Số test |
|---|---|---|
| saucedemo.com | UI (Login, Products, Cart, Checkout, Logout) | ... |
| restful-booker.herokuapp.com | API (Auth, CRUD Booking) | ... |

Danh sách 72 test case manual và lý do chọn 27 case để automate nằm ở `docs/TestCases.xlsx`.

## Cấu trúc thư mục

```
pages/        Page Object Model (mỗi trang một class)
api/          Client gọi API
tests/ui/     Test giao diện
tests/api/    Test API
conftest.py   Fixture dùng chung, hook chụp ảnh khi fail
pytest.ini    Cấu hình, marker
```

## Cài đặt

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
playwright install
```

## Chạy test

```
pytest                      # chạy tất cả
pytest -m smoke             # chỉ smoke test
pytest -m api               # chỉ API
pytest --headed --slowmo 800    # xem trình duyệt chạy chậm
pytest --html=reports/report.html --self-contained-html   # xuất báo cáo
```

## Điểm kỹ thuật

- Page Object Model: locator tách khỏi test, đổi UI chỉ sửa một chỗ
- Data-driven bằng `@pytest.mark.parametrize`
- Fixture cho setup/teardown, test độc lập nhau
- Không dùng `sleep`, dựa vào cơ chế auto-wait của Playwright
- API test có fixture token và tự dọn dữ liệu sau test
- CI chạy tự động, lưu báo cáo và trace khi test fail