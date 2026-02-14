# Bug Reports - SauceDemo

> Note: These are sample bug reports written in a professional format for portfolio purposes.

---

## BUG-001: Login error message is not specific when password is wrong
**Module/Feature:** Login  
**Environment:** Windows 10/11 - Chrome (latest)  
**Severity:** Medium  
**Priority:** P2  
**Reporter:** Sami  
**Date:** (add today)

### Steps to Reproduce
1. Open https://www.saucedemo.com
2. Enter username: `standard_user`
3. Enter password: `wrong_pass`
4. Click **Login**

### Expected Result
A clear error message indicates that the password is incorrect (or credentials are invalid) and guides the user.

### Actual Result
A generic error message is shown (not specific about what is wrong).

### Evidence
(Add screenshot if available)

### Notes
Improving error messaging helps users recover faster and reduces support tickets.

---

## BUG-002: Checkout button is accessible even when cart is empty
**Module/Feature:** Cart  
**Environment:** Windows 10/11 - Chrome (latest)  
**Severity:** High  
**Priority:** P1  
**Reporter:** Sami  
**Date:** (add today)

### Steps to Reproduce
1. Login with valid credentials
2. Go to **Cart**
3. Ensure cart is empty (no items)
4. Observe the **Checkout** button

### Expected Result
Checkout should be disabled/hidden when cart is empty OR user should be blocked with a clear message.

### Actual Result
Checkout action is still available even with an empty cart.

### Evidence
(Add screenshot if available)

### Notes
This can lead to invalid checkout flow and confusing user experience.

---

## BUG-003: Sorting dropdown selection does not persist after returning from product details
**Module/Feature:** Products - Sorting  
**Environment:** Windows 10/11 - Chrome (latest)  
**Severity:** Low  
**Priority:** P3  
**Reporter:** Sami  
**Date:** (add today)

### Steps to Reproduce
1. Login with valid credentials
2. On Products page, set sorting to **Price (low to high)**
3. Open any product details page
4. Click **Back to products**

### Expected Result
Sorting selection should remain the same (low to high) after navigation.

### Actual Result
Sorting resets to default after returning to Products page.

### Evidence
(Add screenshot if available)

### Notes
Minor UX issue but affects user consistency.
