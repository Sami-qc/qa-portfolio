# 🧪 API Test Cases

## 🔐 Authentication Test Cases

| ID | Test Scenario | Steps | Expected Result |
|----|---------------|-------|-----------------|
| TC_AUTH_001 | Valid login | Send `POST` request to `/auth/login` with valid username and password in request body | Status `200 OK` and response contains authentication token |
| TC_AUTH_002 | Invalid login | Send `POST` request to `/auth/login` with invalid username or password in request body | Error response is returned and login is rejected |
| TC_AUTH_003 | Empty credentials | Send `POST` request to `/auth/login` with empty username and password fields | Error response is returned for invalid or empty credentials |
| TC_AUTH_004 | Missing password field | Send `POST` request to `/auth/login` with username only and without password field | Error response is returned and request is not processed successfully |

---

## 🛍️ Products Test Cases

| ID | Test Scenario | Steps | Expected Result |
|----|---------------|-------|-----------------|
| TC_PROD_001 | Get all products | Send `GET` request to `/products` | Status `200 OK` and response returns a non-empty list of products |
| TC_PROD_002 | Get product by valid ID | Send `GET` request to `/products/{id}` using a valid product ID | Status `200 OK` and response contains correct product details such as `id`, `title`, and `price` |
| TC_PROD_003 | Get product by invalid ID | Send `GET` request to `/products/{id}` using an invalid or non-existing product ID | Error response is returned or product is not found |
| TC_PROD_004 | Validate product response structure | Send `GET` request to `/products/{id}` using a valid product ID and inspect the response body | Response contains expected fields such as `id`, `title`, `price`, `description`, `category`, and `image` |
| TC_PROD_005 | Validate product data types | Send `GET` request to `/products/{id}` using a valid product ID and verify field data types | Response fields return correct data types, e.g. `id` as number, `title` as string, and `price` as number |

---

## 🛒 Cart Test Cases

| ID | Test Scenario | Steps | Expected Result |
|----|---------------|-------|-----------------|
| TC_CART_001 | Add product to cart | Send `POST` request to `/carts` with valid user ID, date, and product data in request body | Status `200 OK` or `201 Created` and cart is created successfully |
| TC_CART_002 | Update cart | Send `PUT` request to `/carts/{id}` with updated cart data in request body | Status `200 OK` and response reflects updated cart information |
| TC_CART_003 | Delete cart | Send `DELETE` request to `/carts/{id}` using a valid cart ID | Status `200 OK` and cart is deleted successfully |
| TC_CART_004 | Add invalid product to cart | Send `POST` request to `/carts` with invalid or non-existing product ID in request body | Error response is returned or invalid product is not accepted |
| TC_CART_005 | Empty cart payload | Send `POST` request to `/carts` with empty request body | Error response is returned and cart is not created |

---

## ❗ Negative Test Cases

| ID | Test Scenario | Steps | Expected Result |
|----|---------------|-------|-----------------|
| TC_NEG_001 | Invalid endpoint | Send request to a non-existing API endpoint | Status `404 Not Found` is returned |
| TC_NEG_002 | Unauthorized access | Send request to protected endpoint without valid authentication token | Status `401 Unauthorized` or relevant authorization error is returned |
| TC_NEG_003 | Malformed JSON body | Send request with invalid JSON format in request body | Error response is returned and request is rejected |
| TC_NEG_004 | Invalid data types | Send request with incorrect data types for one or more fields | Validation fails and error response is returned |
| TC_NEG_005 | Missing required fields | Send request without one or more required fields in request body | Error response is returned and request is not processed successfully |
