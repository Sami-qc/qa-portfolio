
# Valid Test Cases — IRAVIN Website

## Feature: Product Detail Page / Cart / Checkout

---

### TC-001
**Title:** Verify product detail page displays all required product information  
**Module:** Product Detail Page  
**Priority:** High  
**Preconditions:**  
1. User is on a valid product detail page  
2. Product is available online  

**Test Data:**  
- Product: Sage Green Textured Knit Relaxed Fit Camp Collar Shirt  
- URL: Product detail page  

**Steps:**  
1. Open the product detail page  
2. Observe the product section  

**Expected Result:**  
The page should display the product name, price, original price, discount badge, savings amount, color option, available sizes, and Add to Cart button.

---

### TC-002
**Title:** Verify user can select an available size  
**Module:** Product Detail Page  
**Priority:** High  
**Preconditions:**  
1. User is on a product detail page  
2. Product has available sizes  

**Test Data:**  
- Size: L  

**Steps:**  
1. Open the product detail page  
2. Click on size "L"  

**Expected Result:**  
The selected size should be highlighted as active.

---

### TC-003
**Title:** Verify user can add a product to cart successfully  
**Module:** Product Detail Page / Cart  
**Priority:** Critical  
**Preconditions:**  
1. User is on a valid product detail page  
2. Product is in stock  
3. A size is selected  

**Test Data:**  
- Product: Sage Green Textured Knit Relaxed Fit Camp Collar Shirt  
- Size: L  

**Steps:**  
1. Open the product detail page  
2. Select size "L"  
3. Click "Add to cart"  
4. Observe the success message or cart update  

**Expected Result:**  
The product should be added to the cart successfully, and a confirmation message or cart update should appear.

---

### TC-004
**Title:** Verify added product appears correctly in cart  
**Module:** Cart  
**Priority:** Critical  
**Preconditions:**  
1. User has added a product to the cart  

**Test Data:**  
- Product: Sage Green Textured Knit Relaxed Fit Camp Collar Shirt  
- Size: L  

**Steps:**  
1. Open the cart page  
2. Review the added product details  

**Expected Result:**  
The cart should show the correct product name, selected size, quantity, original price, discounted price, and total item price.

---

### TC-005
**Title:** Verify cart subtotal is displayed correctly  
**Module:** Cart  
**Priority:** High  
**Preconditions:**  
1. Cart contains one product  

**Test Data:**  
- Product price: 715.00 EGP  

**Steps:**  
1. Open the cart page  
2. Review the estimated total  

**Expected Result:**  
The estimated total should match the discounted item price shown in the cart.

---

### TC-006
**Title:** Verify user can proceed from cart to checkout  
**Module:** Cart / Checkout  
**Priority:** Critical  
**Preconditions:**  
1. Cart contains at least one product  

**Steps:**  
1. Open the cart page  
2. Click the "Check out" button  

**Expected Result:**  
The user should be redirected to the checkout page successfully.

---

### TC-007
**Title:** Verify checkout page displays required contact and delivery fields  
**Module:** Checkout  
**Priority:** Critical  
**Preconditions:**  
1. User has reached the checkout page from cart  

**Steps:**  
1. Open the checkout page  
2. Review the visible form fields  

**Expected Result:**  
The checkout page should display required fields such as email, first name, last name, address, city, governorate, phone number, and payment section.

---

### TC-008
**Title:** Verify shipping methods are displayed on checkout  
**Module:** Checkout  
**Priority:** High  
**Preconditions:**  
1. User is on the checkout page  
2. Delivery address section is visible  

**Steps:**  
1. Open the checkout page  
2. Scroll to the shipping method section  

**Expected Result:**  
Available shipping methods should be displayed with clear labels and prices.

---

### TC-009
**Title:** Verify checkout order summary shows correct product pricing  
**Module:** Checkout  
**Priority:** High  
**Preconditions:**  
1. User is on checkout page with one product in cart  

**Test Data:**  
- Product discounted price: 715.00 EGP  
- Shipping: 57.50 EGP  

**Steps:**  
1. Open the checkout page  
2. Review the order summary section  

**Expected Result:**  
The order summary should display the correct product, subtotal, shipping fee, total amount, and savings.

---

### TC-010
**Title:** Verify shipping fee is added correctly to total  
**Module:** Checkout  
**Priority:** High  
**Preconditions:**  
1. User is on the checkout page  
2. One shipping method is selected  

**Test Data:**  
- Subtotal: 715.00 EGP  
- Shipping: 57.50 EGP  
- Expected total: 772.50 EGP  

**Steps:**  
1. Open checkout  
2. Review subtotal, shipping, and total values  

**Expected Result:**  
The total should equal subtotal plus shipping fee.

---

### TC-011
**Title:** Verify user can enter contact email on checkout  
**Module:** Checkout  
**Priority:** Medium  
**Preconditions:**  
1. User is on checkout page  

**Test Data:**  
- Email: test@example.com  

**Steps:**  
1. Click the email field  
2. Enter a valid email address  

**Expected Result:**  
The email field should accept the value without error.

---

### TC-012
**Title:** Verify available payment method is displayed on checkout  
**Module:** Checkout  
**Priority:** High  
**Preconditions:**  
1. User is on checkout page  

**Steps:**  
1. Scroll to the payment section  

**Expected Result:**  
Available payment methods should be displayed clearly, such as credit card.

---

### TC-013
**Title:** Verify currency is displayed consistently on product, cart, and checkout pages  
**Module:** Product Detail Page / Cart / Checkout  
**Priority:** High  
**Preconditions:**  
1. User can access product page, cart page, and checkout page  

**Steps:**  
1. Open the product detail page  
2. Open the cart page  
3. Open the checkout page  
4. Compare displayed currency format across pages  

**Expected Result:**  
Currency display should be consistent across all pages.

---

### TC-014
**Title:** Verify promotional discount is reflected on product and cart pricing  
**Module:** Product Detail Page / Cart  
**Priority:** High  
**Preconditions:**  
1. User is on a discounted product page  

**Test Data:**  
- Promotion: 45% off  

**Steps:**  
1. Open the product page  
2. Note the original price and discounted price  
3. Add the product to cart  
4. Open cart page  

**Expected Result:**  
The discounted price shown on the product page should match the price shown in the cart.

---

### TC-015
**Title:** Verify user can continue shopping from the cart page  
**Module:** Cart  
**Priority:** Medium  
**Preconditions:**  
1. Cart contains one or more items  

**Steps:**  
1. Open the cart page  
2. Click "Continue shopping"  

**Expected Result:**  
The user should be redirected back to the shopping or collection page.
