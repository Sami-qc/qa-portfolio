# QA Portfolio — Sami Mustafa

![Manual Testing](https://img.shields.io/badge/Manual%20Testing-✓-blue)
![API Testing](https://img.shields.io/badge/API%20Testing-Postman-orange)
![Automation](https://img.shields.io/badge/Automation-Playwright-green)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-black)
![Language](https://img.shields.io/badge/Python-100%25-yellow)

> **Software Test Engineer** with hands-on experience testing **real production applications**, finding critical bugs, and building end-to-end automation frameworks.

---

## 👋 About Me

I'm **Sami Mustafa**, a QA Engineer passionate about breaking software and making it better.

This portfolio is **not built on demo sites**. It's built on **real apps that real users use every day** — local Egyptian e-commerce stores, delivery apps with 50,000+ downloads, and public APIs. Every bug here was found by me, in production, through real testing sessions.

**What you'll find:**
- Real bug reports I filed against production apps (with video evidence)
- Professional Test Plans and Test Cases using IEEE 829 structure
- API test suites with positive and negative scenarios
- End-to-end UI automation using Playwright + Python (POM architecture)
- CI/CD pipelines that run on every commit

---

## 🎯 What This Portfolio Proves

| Skill | Evidence |
|---|---|
| Manual Testing | 20+ test cases, exploratory sessions, traceability matrix |
| Bug Discovery | Real bugs found in Ravin (e-commerce) and Fast App (delivery) |
| Bug Reporting | Jira tickets, Jam.dev recordings, structured reports |
| API Testing | Postman collections with negative tests, schema validation |
| Test Automation | Playwright + Python + Page Object Model |
| CI/CD | GitHub Actions workflows running tests on every push |
| Test Management | Jira SCRUM board, sprint planning, severity/priority |

---

## 🐛 Real Bugs I Found (Production Apps)

### Ravin — Egyptian Fashion E-commerce ([shop.iravin.com](https://shop.iravin.com/))

| ID | Title | Severity | Priority | Type |
|---|---|---|---|---|
| [SCRUM-2](./manual-testing/bug-reports/BUG-001-ravin-localization.md) | Promotional banner text does not fully update on language change | Medium | P2 | UI / Localization |
| [SCRUM-3](./manual-testing/bug-reports/BUG-002-ravin-free-shipping.md) | Free shipping not applied at checkout for orders above 1500 EGP | High | P1 | Business Logic / Pricing |

**Live Jira Board:** [View SCRUM board →](https://samimustafadev.atlassian.net/jira/software/projects/SCRUM/boards/1)

### Fast App — Local Food Delivery (50K+ downloads) ([Google Play](https://play.google.com/store/apps/details?id=com.ZED.zid_app))

See [fast-delivery-app-qa/](./fast-delivery-app-qa/) for bug reports and test artifacts.

---

## 🏗️ Portfolio Structure

```
qa-portfolio/
├── manual-testing/              → Test plans, test cases, bug reports, checklists
│   ├── test-plans/
│   ├── test-cases/
│   ├── bug-reports/
│   └── traceability-matrix.md
│
├── api-testing/                 → Postman collections, Newman CLI, HTML reports
│   ├── collections/
│   ├── environments/
│   ├── reports/
│   └── README.md
│
├── playwright-automation/       → E2E UI automation with POM architecture
│   ├── tests/
│   ├── pages/
│   ├── fixtures/
│   └── playwright.config.py
│
├── ravin-ecommerce-web-qa/      → Real e-commerce testing (shop.iravin.com)
│   ├── test-sessions/
│   ├── bug-reports/
│   └── evidence/
│
├── fast-delivery-app-qa/        → Real mobile app testing (Fast App, Egypt)
│   ├── test-sessions/
│   ├── bug-reports/
│   └── evidence/
│
└── .github/workflows/           → CI/CD pipelines
```

---

## 🛠️ Tech Stack

**Testing Tools**
- Manual: Jira, Confluence, TestRail (concepts), Jam.dev
- API: Postman, Newman, JSON Schema validation
- Automation: Playwright, Python, pytest
- CI/CD: GitHub Actions
- Reporting: Allure, HTML reports

**Languages & Frameworks**
- Python (primary), JavaScript (learning)
- pytest, Playwright, Requests library

**Methodologies**
- Agile / SCRUM
- Test design: Equivalence Partitioning, Boundary Value Analysis, Decision Tables, State Transition
- Risk-based testing
- Exploratory testing (Session-Based Test Management)

---

## 📊 Quick Stats

- **62+** commits of active development
- **2** production apps tested end-to-end
- **5** critical/major bugs reported with evidence
- **20+** test cases documented
- **1** active Jira SCRUM project

---

## 🚀 How to Run the Automation Suite

```bash
# Clone the repo
git clone https://github.com/Sami-qc/qa-portfolio.git
cd qa-portfolio/playwright-automation

# Install dependencies
pip install -r requirements.txt
playwright install

# Run all tests
pytest

# Run with Allure report
pytest --alluredir=./allure-results
allure serve ./allure-results
```

---

## 📬 Contact

- **GitHub:** [@Sami-qc](https://github.com/Sami-qc)
- **Jira Portfolio:** [SCRUM Board](https://samimustafadev.atlassian.net/jira/software/projects/SCRUM/boards/1)
- **Email:** [sami.mustafa.dev@gmail.com
]
- **LinkedIn:** [https://www.linkedin.com/in/sami-mustafa-qc/]

---

## 🎓 Currently Learning

- Playwright with TypeScript
- Performance testing with k6
- CI/CD deep-dives (GitHub Actions advanced)
- 

---

> *"Quality is never an accident; it is always the result of intelligent effort."* — John Ruskin

**Open to Junior QA Engineer / Junior Software Test Engineer positions (local & remote).**
