# Valid Test Cases — Fast App

## Feature: Order Cancellation — Proposed Expected Behavior

---

### TC-001
**Title:** Verify user can cancel an order immediately after placing it  
**Precondition:** User has placed an order successfully and the order is still in an eligible cancellation state  
**Steps:**
1. Go to Current Orders
2. Open the active order
3. Click "Cancel Order"
4. Confirm cancellation  
**Expected Result:**  
The order is canceled successfully, and the status updates to "Cancelled"

---

### TC-002
**Title:** Verify the Cancel Order button is visible in early order states  
**Precondition:** Order status is "Received" or "Confirmed"  
**Steps:**
1. Open order details  
**Expected Result:**  
The Cancel Order button should be visible and enabled

---

### TC-003
**Title:** Verify a confirmation message appears before cancellation  
**Steps:**
1. Click "Cancel Order"  
**Expected Result:**  
A confirmation message should appear asking the user to confirm the cancellation

---

### TC-004
**Title:** Verify order status updates after cancellation  
**Precondition:** Order is in an eligible cancellation state  
**Steps:**
1. Open the active order
2. Click "Cancel Order"
3. Confirm cancellation  
**Expected Result:**  
The order status should change to "Cancelled"

---

### TC-005
**Title:** Verify user cannot cancel an order after it is out for delivery  
**Precondition:** Order status is "Out for Delivery"  
**Steps:**
1. Open the active order  
**Expected Result:**  
The Cancel Order action should not be available to the user

---

### TC-006
**Title:** Verify refund process is triggered for online payment after cancellation  
**Precondition:** Order was paid online and is still in an eligible cancellation state  
**Steps:**
1. Open the active order
2. Click "Cancel Order"
3. Confirm cancellation  
**Expected Result:**  
The refund process should be initiated, and the user should see a message indicating that the refund is being processed

---

### TC-007
**Title:** Verify the system processes restaurant notification after cancellation  
**Precondition:** Order is successfully canceled  
**Steps:**
1. Cancel the order from the order details page  
**Expected Result:**  
The system should process the cancellation successfully and update the order status accordingly
