# QA Automation Portfolio

End-to-end automated testing suite for an e-commerce web application (SauceDemo), covering **four testing layers**: UI automation, API testing, database verification, and continuous integration.

Built with Python, Playwright, PyTest, Postman and GitHub Actions.

[![Tests](https://github.com/greatman-786/qa-portfolio/actions/workflows/tests.yml/badge.svg)](https://github.com/greatman-786/qa-portfolio/actions)

---

## Overview

This project automates the critical journeys a real user takes on an e-commerce site — from logging in to completing a purchase — and verifies each step behaves correctly. It tests both the "happy path" (everything works) and negative cases (invalid inputs handled properly), reflecting real-world QA practice.

Testing doesn't stop at the interface. This suite also checks the API responses and confirms that data is genuinely saved to the database — because a success message on screen is not proof that anything was stored.

---

## Testing Layers Covered

| Layer | What It Verifies | Tool |
|---|---|---|
| **UI / End-to-end** | User journeys work in a real browser | Playwright + PyTest |
| **API** | Endpoints return correct status codes and data | Postman |
| **Database** | Data is actually persisted correctly | SQLite + PyTest |
| **Continuous Integration** | Every code change is tested automatically | GitHub Actions |

---

## 1. UI Automation — `test_saucedemo.py`

Five automated end-to-end tests covering the core e-commerce flow:

| # | Test | What It Verifies |
|---|---|---|
| 1 | `test_login_page_loads` | The login form renders correctly |
| 2 | `test_valid_login` | Correct credentials reach the products page |
| 3 | `test_invalid_login` | Wrong credentials are rejected with a clear error |
| 4 | `test_add_to_cart` | Items are added and the cart badge updates |
| 5 | `test_checkout` | Full flow: cart → checkout → details → order confirmed |

**Testing approach:**
- Covers both positive cases (valid flows) and negative cases (invalid logins, empty fields)
- Each test is independent and runs from a clean state
- Uses specific, reliable locators (e.g. `.shopping_cart_badge`) rather than loose text matching, to avoid flaky tests and strict-mode violations
- Mirrors genuine user journeys end to end

---

## 2. Database Testing — `test_database.py`

Verifies that data reaching the interface is actually stored correctly:

- Connects to the database
- Inserts a record
- Queries it back with a `SELECT`
- Asserts the record genuinely exists
- Closes the connection cleanly

This covers the gap that UI tests can't see: the screen may say "success" while nothing was saved.

---

## 3. API Testing — Postman

REST endpoints validated directly, independent of the interface:

- `GET` requests checked for correct status codes (`200 OK` on valid requests, `404` on invalid paths)
- Response structure and content verified
- Assertion scripts written in Postman's test tab to check results automatically:

```javascript
pm.test("Status is 200", function () {
    pm.response.to.have.status(200);
});
```

---

## 4. CI/CD Pipeline — GitHub Actions

A workflow at `.github/workflows/tests.yml` runs the entire suite automatically on **every push**:

1. Spins up a clean Ubuntu environment
2. Installs Python 3.11 and dependencies
3. Installs the Playwright Chromium browser
4. Runs all UI and database tests
5. Reports pass/fail status

This means no code change goes unverified. Live run history is visible in the [**Actions**](https://github.com/greatman-786/qa-portfolio/actions) tab.

---

## Manual Testing

Alongside automation, this portfolio is backed by structured manual testing practice:

- **Test case design** — written cases covering login, cart, checkout, and edge conditions
- **Exploratory testing** — 15+ UI elements tested including forms, dropdowns, file uploads, JavaScript alerts, drag-and-drop, dynamic loading, hovers and sliders
- **Bug reporting** — real defects found and documented with reproducible steps, severity, and expected vs actual behaviour, including a server-side signup failure discovered on a live production app

Automation catches regressions; manual testing catches what nobody thought to automate. Both matter.

---

## Tech Stack

- **Python** — core language
- **Playwright** — modern browser automation
- **PyTest** — test framework and runner
- **SQLite** — database testing
- **Postman** — API testing
- **GitHub Actions** — CI/CD

---

## How to Run

Install dependencies:

```bash
pip install pytest-playwright
playwright install
```

Run the UI tests:

```bash
pytest test_saucedemo.py -v
```

Run the database tests:

```bash
pytest test_database.py -v
```

Run everything:

```bash
pytest -v
```

---

## About

Built as a hands-on QA project to demonstrate practical, verifiable testing skills across the full stack — not just clicking through a browser, but validating the API and database layers underneath, with automation wired into CI so it runs continuously.

Everything here is public and reproducible. The tests genuinely run, and the pipeline genuinely passes.

**Asad Ullah** — AI Automation & QA Specialist
📍 Sialkot, Pakistan
🔗 [Portfolio](https://asad-portfolio-drab.vercel.app) · [LinkedIn](https://www.linkedin.com/in/asad-ullah-b0190a236) · [GitHub](https://github.com/greatman-786)
📩 asadullah541989@gmail.com
