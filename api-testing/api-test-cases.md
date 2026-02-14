# API Test Cases – Sample Project

## API Information
- API Name: (Put API name here)
- Base URL: (e.g., https://api.example.com)
- Authentication: (None / API Key / Bearer Token / Basic)

---

## TC-API-001: Get All Users

**Method:** GET  
**Endpoint:** /users  
**Precondition:** Valid authentication token (if required)

### Steps
1. Send GET request to `/users`
2. Include required headers (Authorization, Content-Type)

### Expected Result
- Status Code: 200 OK
- Response body contains list of users
- Response time < 2 seconds

---

## TC-API-002: Get User by ID (Valid ID)

**Method:** GET  
**Endpoint:** /users/{id}

### Steps
1. Send GET request with valid user ID
2. Observe response

### Expected Result
- Status Code: 200 OK
- Correct user data returned
- ID matches requested ID

---

## TC-API-003: Get User by ID (Invalid ID)

**Method:** GET  
**Endpoint:** /users/{id}

### Steps
1. Send GET request with non-existing ID

### Expected Result
- Status Code: 404 Not Found
- Proper error message returned

---

## TC-API-004: Create New User

**Method:** POST  
**Endpoint:** /users  

### Steps
1. Send POST request with valid JSON body
2. Include required headers

### Expected Result
- Status Code: 201 Created
- New user returned in response
- ID generated
