# Analytics Dashboard Automation Framework

A Selenium WebDriver automation framework created to practice and improve UI regression testing skills using Python, pytest, and Page Object Model design principles.
## Technologies Used

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- GitHub Actions
- pytest-html

---

## Current Framework Capabilities

- UI automation testing
- Positive and negative login validation
- Explicit waits for synchronization handling
- Page Object Model framework design
- Reusable pytest fixtures
- Screenshot capture on test failure
- HTML test reporting
- GitHub Actions CI pipeline integration

---

## Project Structure

```text
analytics-dashboard-automation/
│
├── .github/workflows/
├── pages/
├── tests/
├── utils/
├── screenshots/
├── reports/
├── conftest.py
├── requirements.txt
└── README.md
```

---

## Test Scenarios

### Positive Login Test
- Validates successful login workflow
- Confirms dashboard page navigation

### Negative Login Test
- Validates invalid credential handling
- Confirms error message visibility

---

## Running Tests

Install dependencies:

```bash
pip install -r requirements.txt
```

Run tests:

```bash
pytest -v
```

Generate HTML report:

```bash
pytest -v --html=reports/report.html --self-contained-html
```

---

## CI/CD Integration

GitHub Actions workflow automatically executes Selenium tests on:
- push events
- pull requests

## Synchronization Strategy

The framework uses Selenium explicit waits to improve test stability and handle dynamic page loading behaviour.
---

## Future Improvements

- Data-driven testing
- Additional dashboard validation scenarios
- Logging integration
- Cross-browser execution