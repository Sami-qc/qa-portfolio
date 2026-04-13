# Valid Test Cases — Fast App

## Feature: Order Cancellation (Expected Behavior)

---

### TC-001
**Title:** Verify user can cancel order immediately after placing it  
**Precondition:** User placed an order successfully  
**Steps:**
1. Go to Current Orders
2. Open the active order
3. Click "Cancel Order"
4. Confirm cancellation  
**Expected Result:**  
Order is canceled successfully and status updates to "Cancelled"

---

### TC-002
**Title:** Verify cancel button is visible in early order state  
**Precondition:** Order status = Received / Confirmed  
**Steps:**
1. Open order details  
**Expected Result:**  
Cancel button should be visible and enabled

---

### TC-003
**Title:** Verify confirmation popup appears before cancellation  
**Steps:**
1. Click Cancel Order  
**Expected Result:**  
Confirmation modal should appear asking user to confirm

---

### TC-004
**Title:** Verify order status updates after cancellation  
**Steps:**
1. Cancel order  
**Expected Result:**  
Order status should change to "Cancelled"

---

### TC-005
**Title:** Verify user cannot cancel after order is out for delivery  
**Precondition:** Order status = Out for delivery  
**Steps:**
1. Open order  
**Expected Result:**  
Cancel button should not be visible or disabled

---

### TC-006
**Title:** Verify refund process is triggered for online payment  
**Precondition:** Order paid via card  
**Steps:**
1. Cancel order  
**Expected Result:**  
Refund process is initiated and user sees refund message

---

### TC-007
**Title:** Verify restaurant is notified after cancellation  
**Steps:**
1. Cancel order  
**Expected Result:**  
Restaurant receives cancellation request
