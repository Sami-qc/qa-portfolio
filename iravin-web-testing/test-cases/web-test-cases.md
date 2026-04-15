# Test Cases — IRAVIN Website

## Feature: Search

---

### TC-001
**Title:** Verify user can search for a product  
**Steps:**
1. Enter valid product name in search bar
2. Press search  
**Expected Result:**  
Relevant products should be displayed

---

### TC-002
**Title:** Verify search with invalid keyword  
**Steps:**
1. Enter random text (e.g. "xyz123")  
**Expected Result:**  
No results message should be displayed

---

## Feature: Product Details

---

### TC-003
**Title:** Verify product details page displays correct info  
**Steps:**
1. Open any product  
**Expected Result:**  
Product name, price, and image should be displayed correctly

---

### TC-004
**Title:** Verify Add to Cart button works  
**Steps:**
1. Open product
2. Click "Add to Cart"  
**Expected Result:**  
Product should be added to cart

---

## Feature: Cart

---

### TC-005
**Title:** Verify user can remove product from cart  
**Steps:**
1. Add product to cart
2. Remove it  
**Expected Result:**  
Product should be removed successfully

---

### TC-006
**Title:** Verify cart updates quantity  
**Steps:**
1. Add product
2. Increase quantity  
**Expected Result:**  
Quantity and total price should update correctly
