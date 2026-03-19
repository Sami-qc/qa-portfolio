# 🛒 Fake Store API Testing

## 📌 Project Overview

This project focuses on testing the Fake Store REST API as an E-commerce backend system.

The goal is to validate API functionality, reliability, and error handling using structured test design techniques.

---

## 🎯 Objectives

- Validate core API functionalities (Authentication, Products, Cart)
- Perform positive and negative testing
- Verify response structure and data integrity
- Ensure proper status code handling
- Simulate real-world API testing scenarios

---

## 🧪 Scope of Testing

### 1. Authentication
- Login with valid credentials
- Login with invalid credentials
- Token validation

### 2. Products
- Get all products
- Get product by ID
- Validate product data

### 3. Cart
- Add product to cart
- Update cart
- Delete cart

---

## 🛠️ Tools & Technologies

- Postman
- REST API
- JSON
- Manual API Testing
- HTTP Methods (GET, POST, PUT, DELETE)

---

## 📂 Project Structure

---

## ✅ Test Coverage

- Functional Testing
- Negative Testing
- Edge Case Testing
- Status Code Validation
- Response Validation

---

## 🔍 Validation Strategy

The following validation techniques are applied across all API test cases in the Fake Store API project:

### ✔️ Status Code Validation

* Verify correct HTTP status codes for each request (200, 201, 400, 401, 404)
* Ensure error scenarios return appropriate status codes

### ✔️ Response Structure Validation

* Validate JSON response format
* Ensure all required fields are present in responses (e.g. id, title, price, category)

### ✔️ Data Type Validation

* Verify correct data types for each field:

  * id → number
  * title → string
  * price → number
  * category → string

### ✔️ Data Integrity Validation

* Ensure returned data matches the request input
* Validate product details consistency across endpoints

### ✔️ Negative Testing Validation

* Validate API behavior with:

  * Invalid credentials
  * Missing fields
  * Invalid product IDs
* Ensure proper error messages are returned

### ✔️ Edge Case Validation

* Test API with:

  * Large input values
  * Special characters
  * Null values
  * Boundary conditions

### ✔️ Performance Validation

* Verify API response time is within acceptable limits (less than 2 seconds)


---

## ❗ Negative Testing Approach

Negative testing is performed to ensure the API handles invalid inputs correctly:

- Invalid credentials
- Missing required fields
- Invalid product IDs
- Unauthorized access (missing or invalid token)
- Malformed JSON requests

---

## ⚠️ Risk Areas

High-risk areas covered in this project:

- Authentication (token handling)
- Cart operations (data accuracy)
- Invalid input handling
