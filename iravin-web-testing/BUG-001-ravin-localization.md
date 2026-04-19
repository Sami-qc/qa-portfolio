# 🐛 BUG-001: Promotional banner text does not fully update on language change

---

### 📋 Summary

| Field | Value |
|---|---|
| **Bug ID** | BUG-001 |
| **Jira Ticket** | [SCRUM-2](https://samimustafadev.atlassian.net/jira/software/projects/SCRUM/boards/1) |
| **Reporter** | Sami Mustafa |
| **Date Found** | 2026-04-16 |
| **Status** | Open |
| **Severity** | Medium |
| **Priority** | P2 |
| **Type** | UI / Localization |
| **Component** | Homepage — Promotional Banner |
| **Affected Page** | https://shop.iravin.com/ |

---

### 🎯 Environment

- **Application:** Ravin E-commerce — https://shop.iravin.com/
- **Platform:** Web
- **Browser:** Chrome 147.0.7727.56
- **Operating System:** Windows 10 (x86) 21H2
- **Screen Resolution:** 2400x1191
- **Test Date & Time:** 2026-04-16 17:49 UTC

---

### 📝 Description

When a user switches the website language from Arabic (Egypt | EGP) to English using the language selector, the promotional banner at the top of the homepage does **not** fully translate. Part of the banner remains in the previous language while other parts update, creating an inconsistent bilingual experience on the same element.

---

### 🔁 Steps to Reproduce

1. Open https://shop.iravin.com/ in Chrome
2. Observe the promotional banner at the top of the page (in Arabic by default)
3. Click the language selector in the top-right corner (labeled "Egypt | EGP ج.م")
4. Select **"English"** from the dropdown menu
5. Wait for the page to reload / language to apply
6. Observe the promotional banner text at the top of the page

---

### ✅ Expected Result

The promotional banner text should **fully translate** to English when English is selected. All words, including promotional offers, discount percentages, and currency labels, should appear in English consistently.

---

### ❌ Actual Result

The promotional banner remains **partially in Arabic** or displays **mixed-language content** (some English, some Arabic) after switching the language. The translation is incomplete, leaving users confused about the actual offer.

---

### 💥 Impact / Business Consequence

- **User impact:** Non-Arabic speakers see an unpolished, unprofessional experience. They may miss promotional information because part of it is in a language they don't understand.
- **Business impact:** Reduces trust in the brand's international-readiness. May cause international customers or expats to abandon the site. Damages brand perception for a fashion brand that targets quality-conscious buyers.
- **Frequency:** 100% reproducible on every language switch.

---

### 📎 Evidence

- **Jam.dev Recording:** https://jam.dev/c/e035a987-4db1-4551-a577-4781ea03229f
- **Screen Recording:** `./evidence/BUG-001-recording.webm`
- **Screenshot:** `./evidence/BUG-001-before-switch.png`, `./evidence/BUG-001-after-switch.png`

---

### 🔧 Suggested Fix

The promotional banner likely uses a **hardcoded string** or a **static image with baked-in text** instead of pulling from the i18n (internationalization) translation dictionary. Recommended actions:

1. Audit the banner component to ensure **all text elements** use the same translation source (`i18n.t('banner.promotion')`)
2. If the banner uses an image with text, provide a **locale-specific image** per language (`banner_en.png`, `banner_ar.png`)
3. Add an **automated test** that switches languages and verifies no Arabic characters appear when English is selected (and vice versa)

---

### 🧪 Test Cases That Would Have Caught This

- **TC-001:** Verify all homepage text elements translate completely when switching from Arabic to English
- **TC-002:** Verify all homepage text elements translate completely when switching from English to Arabic
- **TC-003:** Verify promotional banner language matches site language after language toggle
- **TC-004:** Verify no mixed-language content exists on any single UI element
- **TC-005:** Verify currency symbol updates alongside language (EGP ↔ ج.م)

---

### 📊 Reproducibility

- [x] **100%** — Always reproducible on every language switch

---

### 🔗 Related

- **Jam.dev recording:** [https://jam.dev/c/e035a987-4db1-4551-a577-4781ea03229f](https://jam.dev/c/e035a987-4db1-4551-a577-4781ea03229f)
- **Jira Board:** [SCRUM-2](https://samimustafadev.atlassian.net/jira/software/projects/SCRUM/boards/1)
- **Related bug:** BUG-002 (Free shipping not applied — same site)

---
