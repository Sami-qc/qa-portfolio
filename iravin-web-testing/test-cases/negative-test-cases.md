# Negative Test Cases — IRAVIN Website

## Feature: Product Detail Page / Cart

---

### TC-NEG-001
**Title:** Verify user cannot select an unavailable size  
**Module:** Product Detail Page  
**Priority:** High  

**Preconditions:**  
1. Product has at least one unavailable size (disabled)

**Steps:**  
1. Open the product detail page  
2. Try to click on a disabled size  

**Expected Result:**  
The unavailable size should not be selectable and should remain disabled.

---

### TC-NEG-002
**Title:** Verify user cannot add product to cart without selecting size  
**Module:** Product Detail Page  
**Priority:** High  

**Preconditions:**  
1. Product requires size selection  

**Steps:**  
1. Open product detail page  
2. Do not select any size  
3. Click "Add to cart"  

**Expected Result:**  
The system should prevent adding the product and prompt the user to select a size.

---

### TC-NEG-003
**Title:** Verify cart enforces maximum available quantity  
**Module:** Cart  
**Priority:** Critical  

**Preconditions:**  
1. Product has limited stock  

**Steps:**  
1. Add product to cart  
2. Increase quantity beyond available stock  

**Expected Result:**  
The system should limit the quantity and display a message indicating maximum available items.

---

### TC-NEG-004
**Title:** Verify correct message is displayed when quantity exceeds stock  
**Module:** Cart  
**Priority:** High  

**Preconditions:**  
1. Product stock is limited  

**Steps:**  
1. Add product to cart  
2. Increase quantity beyond stock  

**Expected Result:**  
A clear message should appear such as:  
"Only X items were added to your cart due to availability"

---

### TC-NEG-005
**Title:** Verify cart total updates correctly after quantity adjustment limit  
**Module:** Cart  
**Priority:** High  

**Preconditions:**  
1. Quantity was reduced automatically due to stock limit  

**Steps:**  
1. Increase quantity beyond stock  
2. Observe updated quantity and total  

**Expected Result:**  
Cart total should reflect the adjusted valid quantity only.

---

### TC-NEG-006
**Title:** Verify duplicate product with different sizes are handled correctly  
**Module:** Cart  
**Priority:** Medium  

**Preconditions:**  
1. Same product added with different sizes  

**Steps:**  
1. Add product with size S  
2. Add same product with size M  
3. Open cart  

**Expected Result:**  
Each size should appear as a separate cart item.

---

### TC-NEG-007
**Title:** Verify cart does not merge items with different sizes  
**Module:** Cart  
**Priority:** Medium  

**Preconditions:**  
1. Same product exists with different sizes in cart  

**Steps:**  
1. Add product with size S  
2. Add product with size L  

**Expected Result:**  
Items should remain separate and not merged into a single row.

---

### TC-NEG-008
**Title:** Verify cart handles rapid quantity changes correctly  
**Module:** Cart  
**Priority:** Medium  

**Preconditions:**  
1. Product is in cart  

**Steps:**  
1. Click "+" multiple times quickly  
2. Observe quantity and total  

**Expected Result:**  
System should not allow inconsistent values or exceed stock limits.

---

### TC-NEG-009
**Title:** Verify cart handles zero quantity correctly  
**Module:** Cart  
**Priority:** Medium  

**Preconditions:**  
1. Product exists in cart  

**Steps:**  
1. Decrease quantity using "-" button until minimum  

**Expected Result:**  
Quantity should not go below 1 OR item should be removed if allowed.

---

### TC-NEG-010
**Title:** Verify cart item total is displayed correctly for all items  
**Module:** Cart  
**Priority:** High  

**Preconditions:**  
1. Multiple items exist in cart  

**Steps:**  
1. Open cart page  
2. Check each item total price  

**Expected Result:**  
Each item should display correct total (price × quantity) without missing or incorrect values.

---

### TC-NEG-011
**Title:** Verify unavailable product cannot be added after stock runs out  
**Module:** Product Detail Page / Cart  
**Priority:** High  

**Preconditions:**  
1. Product stock becomes zero  

**Steps:**  
1. Attempt to add product to cart  

**Expected Result:**  
System should prevent adding the product and display an out-of-stock message.

---

### TC-NEG-012
**Title:** Verify UI consistency when stock warning message appears  
**Module:** Cart  
**Priority:** Low  

**Preconditions:**  
1. Quantity exceeds stock  

**Steps:**  
1. Trigger stock limit message  
2. Observe UI layout  

**Expected Result:**  
Message should appear clearly without breaking layout or overlapping elements.
