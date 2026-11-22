# QA Automation Portfolio

Automated testing for an e-commerce web application (SauceDemo), covering UI automation, database verification and continuous integration.

Built with Python, Playwright, PyTest and GitHub Actions.

---

## What it covers

This suite automates the journeys a real user takes — logging in, adding to the cart, completing a purchase — and checks each step behaves correctly. It tests the happy path and the negative cases, because the interesting failures are the ones nobody planned for.

It doesn't stop at the interface. A database test confirms data is genuinely written, because a success message on screen is not proof that anything was stored.

| Layer | What it verifies | Tool |
|---|---|---|
| UI / end-to-end | User journeys work in a real browser | Playwright + PyTest |
| Database | Data is actually persisted | SQLite + PyTest |
| Continuous integration | Every push is tested automatically | GitHub Actions |

---

## 1. UI automation — `test_saucedemo.py`

Five end-to-end tests covering the core flow:

| # | Test | What it verifies |
|---|---|---|
| 1 | `test_login_page_loads` | The login form renders correctly |
| 2 | `test_valid_login` | Correct credentials reach the products page |
| 3 | `test_invalid_login` | Wrong credentials are rejected with a clear error |
| 4 | `test_add_to_cart` | Items are added and the cart badge updates |
| 5 | `test_checkout` | Cart → checkout → details → order confirmed |

**Approach:**

- Positive and negative cases, not just the path that works
- Each test independent and starting from a clean state
- Specific locators like `.shopping_cart_badge` rather than loose text matching, which is what keeps a suite from going flaky
- Journeys that mirror what a user actually does

---

## 2. Database testing — `test_database.py`

Confirms that data reaching the interface is actually stored: connects, inserts a record, queries it back with a SELECT, asserts it exists, closes cleanly.

This covers the gap UI tests can't see. The screen can say "success" while nothing was saved — which is a failure mode I've hit for real on another project, where a webhook reported 52 consecutive successes while writing empty rows.

---

## 3. CI/CD — GitHub Actions

A workflow at `.github/workflows/tests.yml` runs the suite on every push:

- Clean Ubuntu environment
- Python 3.11 and dependencies installed
- Playwright Chromium installed
- UI and database tests run
- Pass/fail reported

Run history is public in the [Actions tab](https://github.com/greatman-786/qa-portfolio/actions) — including one red run from August, left there because a history with no failures in it isn't a real history.

---

## How to run it

```bash
pip install pytest-playwright
playwright install
```

```bash
pytest test_saucedemo.py -v     # UI tests
pytest test_database.py -v      # database test
pytest -v                       # everything
```

---

## What isn't in this repo

I've also done manual exploratory testing, written test cases, and documented defects with reproduction steps and severity — including a server-side signup failure found on a live production app. Those documents aren't published here, so take this repo as the automated side only.

The written-up version of that work is in the [AI Voice Agent](https://github.com/greatman-786/ai-voice-agent) repo: 13 test cases, 5 defects, each with cause and fix.

---

**Asad Ullah** — AI automation and QA engineer. Sialkot, Pakistan.
[Portfolio](https://asad-portfolio-drab.vercel.app) · [LinkedIn](https://www.linkedin.com/in/asad-ullah-b0190a236) · asadullah541989@gmail.com
