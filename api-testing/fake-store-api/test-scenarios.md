# 🧪 API Test Scenarios

## 🔐 Authentication Scenarios

* Verify login with valid credentials
* Verify login with invalid credentials
* Verify login with empty username and password
* Verify login with missing fields
* Verify token is returned on successful login

---

## 🛍️ Products Scenarios

* Verify retrieving all products
* Verify retrieving a product by valid ID
* Verify retrieving a product by invalid ID
* Verify product response structure
* Verify product data types

---

## 🛒 Cart Scenarios

* Verify adding product to cart
* Verify updating cart
* Verify deleting cart
* Verify cart with invalid product ID
* Verify cart with empty payload

---

## ❗ Negative Scenarios

* Verify API response with invalid endpoint
* Verify unauthorized access without token
* Verify malformed JSON request
* Verify handling of invalid data types
* Verify missing required fields

---

## ⚠️ Edge Case Scenarios

* Verify API with very large input values
* Verify API with special characters
* Verify API with null values
* Verify API with boundary values
