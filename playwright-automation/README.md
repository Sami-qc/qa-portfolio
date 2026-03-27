# SauceDemo E2E Test Suite

An end-to-end test automation project built with **Playwright + Python**, targeting [SauceDemo](https://www.saucedemo.com) as a real-world e-commerce application.

This project demonstrates my ability to design and implement a maintainable, scalable test framework using the **Page Object Model (POM)** pattern.

---

## Tech Stack

| Tool | Version |
|---|---|
| Python | 3.13 |
| Playwright | 0.72 |
| Pytest | 9.0 |

---

## 📁 Project Structure

```
playwright-automation/
├── flows/                   # High-level user flow scripts
│   ├── __init__.py
│   └── login_flow.py        # End-to-end login flow
├── pages/                   # Page Object Model classes
│   ├── __init__.py
│   ├── base_page.py         # Base class for all pages
│   ├── login_page.py        # Login page interactions
│   ├── cart_page.py         # Cart page interactions
│   └── inventory_page.py    # Inventory/products page interactions
├── tests/                   # Test files
│   ├── __init__.py
│   ├── test_login.py        # Login test scenarios
│   └── test_cart.py         # Cart test scenarios
├── utils/                   # Shared utilities
│   ├── helpers.py           # Helper functions
│   └── test_data.py         # Test data & credentials
├── conftest.py              # Pytest fixtures & browser setup
├── playwright.yml           # GitHub Actions CI workflow
├── pytest.ini               # Pytest configuration
└── README.md
```

---

## Test Scenarios

### Login Tests (`test_login.py`)
- Valid login with standard user credentials
- *(More scenarios coming soon: invalid credentials, locked-out user)*

### Cart Tests (`test_cart.py`)
- *(Cart test scenarios in progress)*

---

## How to Run

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

## Key Concepts Applied

- **Page Object Model (POM)** – separates test logic from UI interactions
- **Base Page Class** – shared methods inherited by all page objects
- **Flow Layer** – high-level user journeys combining multiple page actions
- **Pytest Fixtures** – reusable browser/page setup via `conftest.py`
- **Test Data Separation** – credentials and data stored in `utils/test_data.py`
- **CI/CD Ready** – GitHub Actions workflow configured via `playwright.yml`

---

## Author

**Sami Mustafa**  
Manual & Automation QA Engineer  
sami.mustafa.dev@gmail.com  
[GitHub](https://github.com/Sami-qc) · [LinkedIn](https://www.linkedin.com/in/sami-mustafa-qa)