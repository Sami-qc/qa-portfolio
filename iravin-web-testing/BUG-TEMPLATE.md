# Bug Report Template

> Copy this file, rename it to `BUG-XXX-short-title.md`, and fill in every section.

---

## 🐛 BUG-XXX: [Concise Title — Action + Result]

**Example title:** "Free shipping not applied when order total exceeds 1500 EGP threshold"

---

### 📋 Summary

| Field | Value |
|---|---|
| **Bug ID** | BUG-XXX |
| **Jira Ticket** | [SCRUM-X](link) |
| **Reporter** | Sami Mustafa |
| **Date Found** | YYYY-MM-DD |
| **Status** | Open / In Progress / Fixed / Closed |
| **Severity** | Critical / High / Medium / Low |
| **Priority** | P1 / P2 / P3 / P4 |
| **Type** | Functional / UI / Performance / Security / Localization |
| **Component** | Checkout / Login / Search / Cart / etc. |
| **Affected Version** | e.g., Web v2.4.1 |

---

### 🎯 Environment

- **Application:** [App name + URL]
- **Platform:** Web / Android / iOS
- **Browser:** Chrome 147.0.7727.56
- **Operating System:** Windows 10 (x86) 21H2
- **Screen Resolution:** 2400x1191
- **Network:** Wi-Fi / 4G / etc.
- **Test Date & Time:** YYYY-MM-DD HH:MM UTC

---

### 📝 Description

Brief explanation (2–3 sentences) describing **what** the bug is and **why it matters**.

---

### 🔁 Steps to Reproduce

1. Step one — be specific (include URLs, button names, field values)
2. Step two
3. Step three
4. Step four
5. ...

---

### ✅ Expected Result

What **should** happen based on the requirements, UX logic, or common sense.

---

### ❌ Actual Result

What **actually** happens. Be precise — include error messages, screenshots, or console logs if available.

---

### 💥 Impact / Business Consequence

Explain the real-world impact:
- **User impact:** How does this affect the user's experience?
- **Business impact:** Revenue loss? Trust issues? Support tickets?
- **Frequency:** Does it happen every time, or under specific conditions?

**Example:**
> This bug prevents eligible customers from receiving free shipping, which may cause them to abandon their carts or lose trust in the promotion. Estimated affected orders: any cart ≥ 1500 EGP.

---

### 📎 Evidence

- **Screenshot:** `./evidence/BUG-XXX-screenshot.png`
- **Video:** `./evidence/BUG-XXX-recording.webm` (or Jam.dev link)
- **Console Logs:** `./evidence/BUG-XXX-console.txt`
- **Network Logs:** (if applicable)

---

### 🔧 Suggested Fix (Optional — shows senior thinking)

A short technical hypothesis:
> The cart total calculation likely excludes tax or discounts when comparing against the 1500 EGP threshold. Check the `isEligibleForFreeShipping()` function and verify it uses the correct subtotal field.

---

### 🧪 Test Cases That Would Have Caught This

- **TC-XX:** Verify free shipping applies at boundary value (exactly 1500 EGP)
- **TC-XX:** Verify free shipping applies above threshold (1501 EGP)
- **TC-XX:** Verify free shipping does NOT apply below threshold (1499 EGP)
- **TC-XX:** Verify free shipping calculation with discount codes applied

---

### 📊 Reproducibility

- [ ] 100% — Always reproducible
- [ ] Intermittent — Happens sometimes
- [ ] One-time — Happened once, could not reproduce

---

### 🔗 Related

- **Jam.dev recording:** [link]
- **Related bugs:** BUG-XXX, BUG-YYY
- **Related requirement:** REQ-XX

---
