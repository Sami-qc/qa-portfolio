# 🐞 API Bug Reports

## Bug Report 1

**Bug ID:** BUG_API_001  
**Title:** Login endpoint accepts invalid credentials without proper error handling  
**Module:** Authentication  
**Severity:** High  
**Priority:** High  

### Preconditions
- API server is available
- Authentication endpoint is accessible

### Steps to Reproduce
1. Send `POST` request to `/auth/login`
2. Use invalid username and password in request body
3. Check the API response

### Expected Result
- API should reject invalid credentials
- Proper error message should be returned
- Appropriate status code should be returned

### Actual Result
- API behavior is inconsistent / error handling is unclear

### Notes
- This should be verified against actual API behavior in Postman

---

## Bug Report 2

**Bug ID:** BUG_API_002  
**Title:** Product endpoint does not clearly handle invalid product ID  
**Module:** Products  
**Severity:** Medium  
**Priority:** Medium  

### Preconditions
- Products endpoint is accessible

### Steps to Reproduce
1. Send `GET` request to `/products/{id}`
2. Use invalid or non-existing product ID
3. Check the API response

### Expected Result
- API should return clear error response
- Appropriate status code such as `404 Not Found` should be returned

### Actual Result
- API may return unclear or inconsistent behavior for invalid IDs

### Notes
- Behavior should be validated in execution results

---

## Bug Report 3

**Bug ID:** BUG_API_003  
**Title:** Cart creation accepts invalid product ID in request body  
**Module:** Cart  
**Severity:** High  
**Priority:** High  

### Preconditions
- Cart endpoint is accessible
- Request body contains cart data

### Steps to Reproduce
1. Send `POST` request to `/carts`
2. Provide invalid or non-existing product ID in the request body
3. Submit the request
4. Check the response

### Expected Result
- API should reject invalid product ID
- Error response should be returned
- Cart should not be created successfully

### Actual Result
- API may accept invalid product ID or fail without proper validation

### Notes
- This issue affects data integrity
