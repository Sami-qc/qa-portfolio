# Test Cases - SauceDemo

**Application:** SauceDemo  
**URL:** https://www.saucedemo.com  
**Scope:** Login, Products, Cart, Checkout (basic)  
**Environment:** Windows 10/11 - Chrome (latest)

---

## Login

| ID | Title | Preconditions | Steps | Test Data | Expected Result | Priority |
|---|---|---|---|---|---|---|
| TC-001 | Login with valid credentials | User on login page | 1) Enter username 2) Enter password 3) Click Login | standard_user / secret_sauce | User navigates to Products page | P0 |
| TC-002 | Login with invalid password | User on login page | 1) Enter username 2) Enter wrong password 3) Click Login | standard_user / wrong_pass | Error message displayed, stay on login page | P0 |
| TC-003 | Login with empty username | User on login page | 1) Leave username empty 2) Enter password 3) Click Login | (empty) / secret_sauce | Validation error displayed | P1 |
| TC-004 | Login with empty password | User on login page | 1) Enter username 2) Leave password empty 3) Click Login | standard_user / (empty) | Validation error displayed | P1 |

## Products

| ID | Title | Preconditions | Steps | Test Data | Expected Result | Priority |
|---|---|---|---|---|---|---|
| TC-005 | Products page loads after login | Logged in | 1) Observe Products page | - | Product list visible (names, prices, images) | P0 |
| TC-006 | Sort products by Price (low to high) | Logged in on Products page | 1) Open sort dropdown 2) Select low to high | - | Products sorted lowest to highest | P2 |
| TC-007 | Open product details page | Logged in on Products page | 1) Click product name | Any product | Product details page opens correctly | P2 |
| TC-008 | Add item to cart from Products page | Logged in on Products page | 1) Click "Add to cart" for a product 2) Click cart icon | Any product | Cart contains selected item | P0 |

## Cart & Checkout

| ID | Title | Preconditions | Steps | Test Data | Expected Result | Priority |
|---|---|---|---|---|---|---|
| TC-009 | Remove item from cart | Cart has 1 item | 1) Click "Remove" | - | Item removed from cart | P1 |
| TC-010 | Start checkout flow | Cart has 1 item | 1) Click Checkout | - | Checkout information page opens | P0 |
