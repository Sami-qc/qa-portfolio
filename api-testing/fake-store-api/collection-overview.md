# 📦 API Collection Overview

## 📌 Base URL

`https://fakestoreapi.com`

---

## 🔐 Authentication

The API uses token-based authentication.

### Endpoint:

`POST /auth/login`

### Request Body:

```json
{
  "username": "user",
  "password": "password"
}
```

### Expected Response:

* Status Code: 200 OK
* Returns authentication token

---

## 🛍️ Products Endpoints

### 1. Get All Products

`GET /products`

### 2. Get Product by ID

`GET /products/{id}`

### 3. Get Products by Category

`GET /products/category/{category}`

---

## 🛒 Cart Endpoints

### 1. Get User Cart

`GET /carts/user/{userId}`

### 2. Add New Cart

`POST /carts`

### 3. Update Cart

`PUT /carts/{id}`

### 4. Delete Cart

`DELETE /carts/{id}`

---

## 📊 HTTP Methods Used

* GET → Retrieve data
* POST → Create data
* PUT → Update data
* DELETE → Remove data

---

## ⚠️ Important Notes

* All endpoints return JSON responses
* Proper status code validation is required
* Some endpoints require authentication
* Invalid inputs should be handled gracefully
