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

The following validations are applied across all API tests:

- Status code validation (e.g., 200, 400, 401, 404)
- Response body structure validation
- Data type validation (string, number, boolean)
- Required fields validation
- Response time validation (< 2 seconds)

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
