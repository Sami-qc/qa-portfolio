# 🐛 BUG-002: Free shipping not applied at checkout for orders above 1500 EGP

---

### 📋 Summary

| Field | Value |
|---|---|
| **Bug ID** | BUG-002 |
| **Jira Ticket** | [SCRUM-3](https://samimustafadev.atlassian.net/jira/software/projects/SCRUM/boards/1) |
| **Reporter** | Sami Mustafa |
| **Date Found** | 2026-04-16 |
| **Status** | Open |
| **Severity** | **High** |
| **Priority** | **P1** |
| **Type** | Functional / Business Logic / Pricing |
| **Component** | Checkout — Shipping Calculation |
| **Affected Page** | https://shop.iravin.com/ (Checkout flow) |

---

### 🎯 Environment

- **Application:** Ravin E-commerce — https://shop.iravin.com/
- **Platform:** Web
- **Browser:** Chrome 147.0.7727.56
- **Operating System:** Windows 10 (x86) 21H2
- **Screen Resolution:** 2400x1191
- **Test Date & Time:** 2026-04-16 18:01 UTC

---

### 📝 Description

The website **advertises free shipping for orders over 1500 EGP** via the top promotional banner ("Free Shipping on Orders Over 1,500EGP"). However, during checkout, when the cart total exceeds 1500 EGP, **free shipping is not applied**. Additionally, when the user selects a shipping option, the **total price does not update** to reflect the selection.

This is a **critical pricing/business-logic bug** that directly contradicts the promotion advertised to users.

---

### 🔁 Steps to Reproduce

1. Open https://shop.iravin.com/ in Chrome
2. Note the promotional banner at the top: *"Free Shipping on Orders Over 1,500EGP"*
3. Add items to the cart until the cart subtotal exceeds **1500 EGP**
4. Proceed to checkout
5. Observe the shipping options and the displayed total price
6. Select any shipping option from the available list
7. Observe the total price again

---

### ✅ Expected Result

- Since the cart total exceeds the 1500 EGP threshold, shipping should be **automatically set to free** (0 EGP)
- If a user manually selects a shipping option, the **total price should update** in real time to reflect the new shipping cost (or confirm free shipping)
- The promotion advertised on the homepage should match the actual checkout behavior

---

### ❌ Actual Result

- Free shipping is **not applied** despite the cart total exceeding 1500 EGP
- When a shipping option is selected, the **total price does not update** in the UI
- The user is charged for shipping even though they qualify for the free-shipping promotion

---

### 💥 Impact / Business Consequence

- **User impact:** Customers are **charged incorrectly** for shipping, breaking the promise advertised on the homepage. This creates distrust and may cause cart abandonment at the final step of purchase.
- **Business impact:**
  - **Direct revenue risk:** Customers who notice the discrepancy may dispute the charge, request refunds, or file complaints.
  - **Legal/consumer-protection risk:** False advertising claims — the site promotes free shipping on a condition that isn't enforced.
  - **Trust damage:** This is a **high-visibility bug** on the final page of the purchase funnel — the worst possible place for a bug.
  - **Support load:** Customer support tickets about "why wasn't my shipping free?" will increase.
- **Frequency:** 100% reproducible for any cart ≥ 1500 EGP.

---

### 📎 Evidence

- **Jam.dev Recording:** https://jam.dev/c/231d5de9-50fb-4f05-a9e5-205c7c7ccdc5
- **Screen Recording:** `./evidence/BUG-002-checkout-recording.webm`
- **Screenshot of banner:** `./evidence/BUG-002-promotion-banner.png`
- **Screenshot of checkout:** `./evidence/BUG-002-checkout-no-free-shipping.png`

---

### 🔧 Suggested Fix

Two separate issues to address:

1. **Free-shipping threshold not enforced**
   - Verify the `isEligibleForFreeShipping(cartTotal)` function correctly compares against 1500 EGP
   - Check whether tax, discounts, or coupons are being subtracted before the threshold check (they may be, causing a cart of 1550 EGP after discount to evaluate as below threshold)
   - Confirm the backend returns the correct `free_shipping_eligible: true` flag when applicable

2. **Total not updating on shipping selection**
   - The checkout page is likely missing a **re-render / state update** after the shipping option changes
   - Check the event handler bound to the shipping radio buttons / dropdown
   - Verify the cart total calculation is triggered on `onChange` of shipping selection

**Regression test to add permanently:**
- Automated E2E test at 1499, 1500, and 1501 EGP thresholds
- API-level test for shipping-calculation endpoint

---

### 🧪 Test Cases That Would Have Caught This

- **TC-010:** Verify free shipping is applied when cart total = 1500 EGP (exact boundary)
- **TC-011:** Verify free shipping is applied when cart total = 1501 EGP (just above)
- **TC-012:** Verify free shipping is NOT applied when cart total = 1499 EGP (just below)
- **TC-013:** Verify free shipping is applied when cart total = 3000 EGP (well above)
- **TC-014:** Verify total price updates immediately when shipping option changes
- **TC-015:** Verify free shipping calculation is consistent between homepage promotion and checkout
- **TC-016:** Verify free shipping applies correctly when a discount code is used (edge case)
- **TC-017:** Verify shipping fee recalculates correctly when cart items are removed after threshold is reached

---

### 📊 Reproducibility

- [x] **100%** — Always reproducible for any cart above 1500 EGP

---

### 🔗 Related

- **Jam.dev recording:** [https://jam.dev/c/231d5de9-50fb-4f05-a9e5-205c7c7ccdc5](https://jam.dev/c/231d5de9-50fb-4f05-a9e5-205c7c7ccdc5)
- **Jira Board:** [SCRUM-3](https://samimustafadev.atlassian.net/jira/software/projects/SCRUM/boards/1)
- **Related bug:** BUG-001 (Localization issue — same site)
- **Related requirement:** REQ-CHK-004 — Free shipping threshold enforcement

---

### ⚠️ Severity Justification

**Why "High" and not "Medium":**
- Directly affects the **revenue funnel** (checkout page)
- Contradicts an **advertised promotion** (legal/trust issue)
- Bug is **always reproducible**, not edge-case
- Affects **every customer** qualifying for the promotion

**Why "P1" priority:**
- Should be fixed in the next hotfix cycle, not the next sprint
- Every day this exists = lost customer trust + potential complaints

---
