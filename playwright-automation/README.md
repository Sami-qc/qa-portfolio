#  Playwright Test Automation – SauceDemo


![Playwright Tests](https://github.com/Sami-qc/qa-portfolio/actions/workflows/playwright.yml/badge.svg)


An end-to-end test automation project built with **Playwright + Python**, targeting [SauceDemo](https://www.saucedemo.com) as a real-world e-commerce application.

This project demonstrates my ability to design and implement a maintainable, scalable test framework using the **Page Object Model (POM)** pattern.

---

##  Tech Stack

| Tool | Version |
|---|---|
| Python | 3.13 |
| Playwright | 0.72 |
| Pytest | 9.0 |

---

## 📁 Project Structure

```
playwright-automation/
├── pages/                  # Page Object Model classes
│   ├── login_page.py       # Login page interactions
│   ├── cart_page.py        # Cart page interactions
│   └── inventory_page.py   # Inventory/products page interactions
├── tests/                  # Test files
│   ├── test_login.py       # Login test scenarios
│   └── test_cart.py        # Cart test scenarios
├── utils/                  # Shared utilities
│   └── helpers.py
├── conftest.py             # Pytest fixtures & browser setup
└── README.md
```

---

##  Test Scenarios

 ### 🔐 Login Tests (`test_login.py`)
- Valid login with standard user credentials
- Invalid password shows error message
- Locked out user shows locked out error
- Empty username shows required field error
- Empty password shows required field error

### 🛒 Cart Tests (`test_cart.py`)
- Add item to cart → badge shows 1
- Add 2 items → badge updates to 2
- Remove item from cart → badge disappears
- Navigate to cart → added item appears

---

##  How to Run

**1. Clone the repo**
```bash

git clone https://github.com/Sami-qc/qa-portfolio.git
cd qa-portfolio/playwright-automation

```

**2. Install dependencies**
```bash
pip install pytest pytest-playwright
playwright install
```

**3. Run all tests**
```bash
python -m pytest tests/ -s
```

**4. Run a specific test file**
```bash
python -m pytest tests/test_login.py -s
```

---

##  Key Concepts Applied

- **Page Object Model (POM)** – separates test logic from UI interactions
- **Pytest Fixtures** – reusable browser/page setup via `conftest.py`
- **Assertions** – URL and element state validation with Playwright's `expect()`

---

##  Author

**Samy Mustafa**  
Manual & Automation QA Tester  
 sami.mustafa.dev@gmail.com
 