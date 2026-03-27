#  Playwright Test Automation – SauceDemo


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
Playwright Test V2/
├── pageس/                  # Page Object Model classes
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

###  Login Tests (`test_login.py`)
- Valid login with standard user credentials
- *(More scenarios coming soon: invalid credentials, locked-out user)*

###  Cart Tests (`test_cart.py`)
- *(Cart test scenarios)*

---

##  How to Run

**1. Clone the repo**
```bash
git clone https://github.com/YOUR_USERNAME/playwright-test-v2.git
cd playwright-test-v2
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
 