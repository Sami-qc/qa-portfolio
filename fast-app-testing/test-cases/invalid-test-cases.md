# Invalid / Negative Test Cases — Fast App

## Feature: Order Cancellation — Proposed Expected Behavior

---

### TC-NEG-001
**Title:** Verify user cannot cancel an order that is already out for delivery  
**Precondition:** Order status is "Out for Delivery"  
**Steps:**
1. Go to Current Orders
2. Open the active order  
**Expected Result:**  
The Cancel Order action should not be available to the user

---

### TC-NEG-002
**Title:** Verify user cannot cancel an order that has already been delivered  
**Precondition:** Order status is "Delivered"  
**Steps:**
1. Open order details  
**Expected Result:**  
The Cancel Order action should not be available to the user

---

### TC-NEG-003
**Title:** Verify user cannot submit cancellation without confirmation  
**Precondition:** Order is in an eligible cancellation state  
**Steps:**
1. Open the active order
2. Click "Cancel Order"
3. Close the confirmation popup or select cancel  
**Expected Result:**  
The order should remain active and no cancellation should be processed

---

### TC-NEG-004
**Title:** Verify order remains unchanged if the user dismisses the cancellation message  
**Precondition:** Order is in an eligible cancellation state  
**Steps:**
1. Open the active order
2. Click "Cancel Order"
3. Dismiss the confirmation message  
**Expected Result:**  
The order status should remain unchanged

---

### TC-NEG-005
**Title:** Verify duplicate cancellation requests are prevented  
**Precondition:** Order is in an eligible cancellation state  
**Steps:**
1. Open the active order
2. Tap "Cancel Order" multiple times quickly
3. Confirm cancellation  
**Expected Result:**  
Only one cancellation request should be processed

---

### TC-NEG-006
**Title:** Verify proper behavior when internet connection is lost during cancellation  
**Precondition:** Order is in an eligible cancellation state  
**Steps:**
1. Open the active order
2. Click "Cancel Order"
3. Disable internet connection
4. Confirm cancellation  
**Expected Result:**  
An error message should appear, and the order should remain unchanged unless cancellation is confirmed by the server

---

### TC-NEG-007
**Title:** Verify user sees proper message when cancellation is no longer allowed  
**Precondition:** Order status changes to a non-cancellable state before confirmation  
**Steps:**
1. Open the active order
2. Click "Cancel Order"
3. Confirm cancellation after the order status has changed  
**Expected Result:**  
The system should prevent cancellation and display a clear message explaining that the order can no longer be canceled

---

### TC-NEG-008
**Title:** Verify cancellation is not processed twice from multiple sessions  
**Precondition:** User is logged into the same account on two devices, and the order is in an eligible cancellation state  
**Steps:**
1. Open the same active order on both devices
2. Cancel the order from the first device
3. Attempt to cancel the same order from the second device  
**Expected Result:**  
The system should process only the first successful cancellation request and reject the second request appropriately

---

### TC-NEG-009
**Title:** Verify user cannot cancel using stale order screen data  
**Precondition:** Order status has changed in the backend, but the old order screen is still open  
**Steps:**
1. Open the active order
2. Leave the order screen open
3. Let the order status change to a non-cancellable state
4. Attempt cancellation from the stale screen  
**Expected Result:**  
The system should validate the latest order status and prevent cancellation if the order is no longer eligible

---

### TC-NEG-010
**Title:** Verify refund is not triggered when cancellation fails  
**Precondition:** Order was paid online, but cancellation request is rejected  
**Steps:**
1. Attempt to cancel an online-paid order in a non-eligible state  
**Expected Result:**  
No refund process should be initiated if cancellation is not successful
