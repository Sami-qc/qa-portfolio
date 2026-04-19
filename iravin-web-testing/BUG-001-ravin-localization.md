#  BUG-001: Free shipping value is different in Arabic and English banner

---

##  Summary

| Field | Value |
|---|---|
| **Bug ID** | BUG-001 |
| **Jira Ticket** | [SCRUM-2](https://samimustafadev.atlassian.net/jira/software/projects/SCRUM/boards/1) |
| **Reporter** | Sami Mustafa |
| **Date Found** | 2026-04-16 |
| **Status** | Open |
| **Severity** | High |
| **Priority** | P1 |
| **Type** | Localization / Content Issue |
| **Component** | Homepage Promotional Banner |
| **Affected Page** | https://shop.iravin.com/ |

---

##  Environment

- **Application:** Ravin E-commerce
- **Platform:** Web
- **Browser:** Chrome 147.0.7727.56
- **Operating System:** Windows 10
- **Screen Resolution:** 2400x1191
- **Test Date & Time:** 2026-04-16 17:49 UTC

---

##  Description

The homepage promotional banner shows **different free shipping values** depending on the selected language.

- In **Arabic**, the banner says free shipping is available for orders above **2000 EGP**
- In **English**, the banner says free shipping is available for orders over **1500 EGP**

This means the same offer is shown with two different values, which can confuse users and make the shipping policy unclear.

---

##  Steps to Reproduce

1. Open https://shop.iravin.com/
2. Check the promotional banner while the website is in **Arabic**
3. Notice the free shipping value shown in the banner
4. Change the language to **English**
5. Check the promotional banner again
6. Compare the free shipping value in both languages

---

##  Expected Result

The free shipping value should be the **same in all languages**.  
Changing the language should only translate the text, not change the offer itself.

---

##  Actual Result

The free shipping value is different in each language:

- **Arabic:** 2000 EGP
- **English:** 1500 EGP

---

##  Impact

- Users may not know which free shipping value is correct
- Customers may lose trust in the offer
- This can cause confusion before checkout
- The website looks inconsistent and unreliable

---

##  Evidence

- **Jam.dev Recording:** https://jam.dev/c/e035a987-4db1-4551-a577-4781ea03229f
- **Screen Recording:** `./evidence/BUG-001-recording.webm`
- **Screenshot:** `./evidence/BUG-001-before-switch.png`
- **Screenshot:** `./evidence/BUG-001-after-switch.png`

---

##  Suggested Fix

- Review the promotional banner content in both Arabic and English
- Make sure the same free shipping value is used in both languages
- Keep the offer value consistent across all localized versions
- Add a test case to check banner content after language switching

---

##  Test Cases That Would Have Caught This

- Verify the promotional banner shows the same offer in Arabic and English
- Verify language change updates only the text language, not the business value
- Verify free shipping values are consistent across all supported languages

---

##  Reproducibility

- [x] **100%** — Issue happens every time when comparing Arabic and English banner content

---

##  Related Links

- **Jam.dev recording:** [Open Jam](https://jam.dev/c/e035a987-4db1-4551-a577-4781ea03229f)
- **Jira Board:** [SCRUM-2](https://samimustafadev.atlassian.net/jira/software/projects/SCRUM/boards/1)
