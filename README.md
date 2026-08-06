# QA Automation Portfolio

End-to-end automated test suite for an e-commerce web application (SauceDemo), built with Python, Playwright, and PyTest. This project demonstrates automated testing of core user journeys, covering both success and failure scenarios.

## Overview

This suite automates the critical flows a real user takes on an e-commerce site — from logging in to completing a purchase — and verifies that each step behaves correctly. It tests both the "happy path" (everything works) and negative cases (wrong inputs handled properly), reflecting real-world QA practice.

## What It Tests

- **Login page loads** — the login form renders correctly
- **Valid login** — correct credentials log the user in and reach the products page
- **Invalid login** — wrong credentials are rejected with a clear error message
- **Add to cart** — items are added and the cart count updates correctly
- **Full checkout flow** — cart → checkout → customer details → order confirmation

## Tools & Tech

- **Python** — core language
- **Playwright** — modern browser automation
- **PyTest** — test framework and runner

## Testing Approach

- Tests both **positive cases** (valid flows) and **negative cases** (invalid logins, edge cases)
- Each test is **independent** and runs from a clean state
- Uses **specific, reliable locators** to avoid flaky tests
- Mirrors real user journeys end to end

## How to Run

Install dependencies:

    pip install pytest-playwright
    playwright install

Run the tests:

    pytest test_saucedemo.py -v

## About

Built as a hands-on QA automation project to demonstrate practical skills in writing, structuring, and debugging automated tests for web applications. The suite reflects how QA is done in real teams — testing user flows, catching failures, and verifying fixes.
# QA Automation Tests
