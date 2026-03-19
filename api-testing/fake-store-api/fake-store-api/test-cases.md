# 🧪 API Test Cases

## 🔐 Authentication Test Cases

| ID          | Test Scenario     | Steps                                              | Expected Result               |
| ----------- | ----------------- | -------------------------------------------------- | ----------------------------- |
| TC_AUTH_001 | Valid login       | Send POST request with valid username and password | Status 200 and token returned |
| TC_AUTH_002 | Invalid login     | Send POST request with invalid credentials         | Status 401 or error message   |
| TC_AUTH_003 | Empty credentials | Send POST request with empty fields                | Status 400                    |
| TC_AUTH_004 | Missing fields    | Send request without password                      | Error response                |

---

## 🛍️ Products Test Cases

| ID          | Test Scenario               | Steps                            | Expected Result              |
| ----------- | --------------------------- | -------------------------------- | ---------------------------- |
| TC_PROD_001 | Get all products            | Send GET request to /products    | Status 200 and list returned |
| TC_PROD_002 | Get product by valid ID     | Send GET request with valid ID   | Correct product returned     |
| TC_PROD_003 | Get product by invalid ID   | Send GET request with invalid ID | Status 404                   |
| TC_PROD_004 | Validate product structure  | Check response fields            | Fields exist and valid       |
| TC_PROD_005 | Validate product data types | Check data types                 | Correct types returned       |

---

## 🛒 Cart Test Cases

| ID          | Test Scenario           | Steps                               | Expected Result   |
| ----------- | ----------------------- | ----------------------------------- | ----------------- |
| TC_CART_001 | Add product to cart     | Send POST request with product data | Status 200 or 201 |
| TC_CART_002 | Update cart             | Send PUT request                    | Cart updated      |
| TC_CART_003 | Delete cart             | Send DELETE request                 | Cart removed      |
| TC_CART_004 | Invalid product in cart | Send invalid product ID             | Error response    |
| TC_CART_005 | Empty cart request      | Send empty payload                  | Status 400        |

---

## ❗ Negative Test Cases

| ID         | Test Scenario           | Steps                      | Expected Result  |
| ---------- | ----------------------- | -------------------------- | ---------------- |
| TC_NEG_001 | Invalid endpoint        | Send request to wrong URL  | Status 404       |
| TC_NEG_002 | Unauthorized access     | Send request without token | Status 401       |
| TC_NEG_003 | Malformed JSON          | Send invalid JSON body     | Error response   |
| TC_NEG_004 | Invalid data types      | Send wrong data types      | Validation error |
| TC_NEG_005 | Missing required fields | Omit required fields       | Status 400       |
