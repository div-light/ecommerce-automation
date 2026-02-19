# E-Commerce Test Automation Framework

A production-quality end-to-end test automation framework built with **Playwright + pytest** against [saucedemo.com](https://www.saucedemo.com), following the **Page Object Model (POM)** design pattern with **Allure** reporting and **GitHub Actions** CI/CD.

---

## Tech Stack

| Tool | Purpose |
|---|---|
| [Playwright](https://playwright.dev/python/) | Browser automation |
| [pytest](https://pytest.org/) | Test runner |
| [pytest-playwright](https://pypi.org/project/pytest-playwright/) | Playwright fixtures for pytest |
| [Allure](https://allurereport.org/) | Test reporting |
| [GitHub Actions](https://github.com/features/actions) | CI/CD pipeline |

---

## Project Structure

```
ecommerce-automation/
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI/CD
├── pages/                      # Page Object Model layer
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── product_detail_page.py
│   ├── cart_page.py
│   ├── checkout_info_page.py
│   ├── checkout_overview_page.py
│   └── checkout_complete_page.py
├── tests/                      # Test suites
│   ├── test_login.py           # 7 tests
│   ├── test_inventory.py       # 7 tests
│   ├── test_cart.py            # 5 tests
│   └── test_checkout.py        # 5 tests
├── data/
│   └── test_data.py            # Centralized test data
├── conftest.py                 # Shared pytest fixtures
├── pytest.ini                  # pytest configuration
└── requirements.txt
```

---

## Setup

### Prerequisites
- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/ecommerce-automation.git
cd ecommerce-automation

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
.venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt

# Install Playwright browser
playwright install chromium
```

---

## Running Tests

### Smoke tests (fast sanity check — 6 tests)
```bash
pytest -m smoke -v
```

### Full test suite (24 tests)
```bash
pytest -v
```

### Specific test file
```bash
pytest tests/test_login.py -v
```

### Specific test
```bash
pytest tests/test_login.py::TestLogin::test_valid_login -v
```

### Headed mode (watch the browser)
```bash
pytest --headed -v
```

### Slow motion (useful for debugging)
```bash
pytest --headed --slowmo=500 -v
```

---

## Test Coverage

### Login (`test_login.py`)
| Test | Marker |
|---|---|
| Valid login with standard_user | smoke |
| Locked-out user shows error | smoke |
| Invalid username shows error | |
| Invalid password shows error | |
| Empty credentials shows error | |
| Empty password shows error | |
| Performance glitch user logs in | regression |

### Inventory (`test_inventory.py`)
| Test | Marker |
|---|---|
| All 6 products displayed | smoke |
| Sort by Name A→Z | |
| Sort by Name Z→A | |
| Sort by Price low→high | |
| Sort by Price high→low | |
| Add to cart from listing | smoke |
| Open product detail page | |

### Cart (`test_cart.py`)
| Test | Marker |
|---|---|
| Add single item to cart | smoke |
| Add multiple items to cart | |
| Remove item from cart | |
| Cart persists after navigation | |
| Continue shopping returns to inventory | |

### Checkout (`test_checkout.py`)
| Test | Marker |
|---|---|
| Full checkout flow end-to-end | smoke |
| Missing first name shows error | |
| Missing last name shows error | |
| Missing postal code shows error | |
| Order confirmation message | regression |

---

## Allure Report

```bash
# Install Allure CLI (one-time)
brew install allure          # macOS
# or: scoop install allure  # Windows

# Run tests (results are auto-saved to allure-results/)
pytest -v

# Open interactive report
allure serve allure-results
```

The report includes test steps, severity levels, pass/fail status, and execution timings.

---

## CI/CD

Every push to `main` and every pull request triggers the GitHub Actions workflow:

1. Sets up Python 3.12
2. Installs dependencies
3. Installs Playwright Chromium browser
4. Runs smoke tests
5. Runs the full suite
6. Uploads Allure results as a downloadable artifact (retained for 30 days)

View results in the **Actions** tab of the GitHub repository.

---

## Test Users (saucedemo.com)

| Username | Password | Behaviour |
|---|---|---|
| `standard_user` | `secret_sauce` | Normal user |
| `locked_out_user` | `secret_sauce` | Login blocked |
| `problem_user` | `secret_sauce` | UI glitches |
| `performance_glitch_user` | `secret_sauce` | Slow page loads |
