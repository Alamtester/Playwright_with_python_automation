# OrangeHRM – Playwright Automation Framework

## 1. Project Overview

This project is developed as part of the technical assessment for the **Sr. QA Analyst position at SimuPhish**.

The objective is to demonstrate practical UI automation testing skills using **Python, Playwright, and Pytest** by automating real-world business workflows in the OrangeHRM application.

The framework follows the **Page Object Model (POM)** design pattern to maintain reusable, readable, and maintainable automation scripts.

**Application Under Test:** OrangeHRM Open Source Demo  
**Application URL:** https://opensource-demo.orangehrmlive.com/web/index.php/auth/login  
**Automation Tool:** Playwright  
**Programming Language:** Python  
**Test Framework:** Pytest  
**Design Pattern:** Page Object Model (POM)

---

## 2. Objectives

The main objectives of this project are:

- Analyze the OrangeHRM web application.
- Identify important business functionalities and user workflows.
- Prepare positive and negative test scenarios.
- Automate login and Admin Creation workflows.
- Validate forms and mandatory field validations.
- Validate navigation across different application modules.
- Implement reusable page classes using POM.
- Generate HTML test execution reports.

---

## 3. Application Modules Covered

The following OrangeHRM modules are considered for automation:

| Module | Testing Coverage |
|---|---|
| Login | Valid login, invalid login, mandatory field validation |
| Dashboard | Dashboard visibility and navigation |
| Admin | Admin Creation and Validating Error message on admin creation |

---

## 4. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Playwright | Browser automation |
| Pytest | Test execution and test management |
| Pytest HTML | HTML execution report generation |
| Chromium | Browser for automation |
| Page Object Model | Reusable automation framework design |

---

## 5. Project Structure

```text
playwright_python_project/
│
├── pages/
│   ├── login_page.py
│   ├── dashboard_page.py
│   ├── admin_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_dashboard.py
│   ├── test_admin.py
│
├── reports/
│
├── conftest.py
├── pytest.ini
└── README.md
```

---

## 6. Prerequisites

Ensure the following software is installed:

1. Python 3.10 or above.
2. Visual Studio Code or PyCharm.
3. Google Chrome or Playwright Chromium.
4. Git (optional).

Check Python installation:

```bash
python --version
```

---

## 7. Installation and Setup

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 3: Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 4: Install Playwright Browser

```bash
playwright-install
```

---

## 8. Test Execution

### Execute All Test Cases

```bash
pytest
```

### Execute Tests with HTML Report

```bash
pytest -v --html=reports/report.html --self-contained-html
```

After execution, open the generated HTML report:

```text
reports/report.html
```

---

## 9. Automation Framework Approach

The framework follows the Page Object Model (POM) design pattern.

### Page Classes

Each application module has a separate page class containing:

- Web element locators.
- Page-specific reusable methods.
- User interaction methods.

### Test Classes

Test scripts are maintained separately inside the `tests/` directory.

Each test script:

- Initializes the required page objects.
- Executes the required business workflow.
- Validates expected results using assertions.
- Reports test execution status through Pytest.

### Assertions

Playwright assertions and Pytest assertions are used to validate application behavior and expected results.

---


## 12. Test Scenario Coverage

The following test scenarios are included in the assessment:

1. Verify OrangeHRM application launch.
2. Verify login with valid credentials.
3. Verify login with invalid credentials.
4. Verify mandatory login field validation.
5. Verify navigation to Admin.
6. Verify navigation to PIM.
7.Verify navigation to Leave.
8.Verify navigation to Time.
9.Verify navigation to Recruitment.
10.Verify navigation to My Info.
11.Verify navigation to Performance.
12.Verify navigation to Dashboard.
13.Verify navigation to Directory.
14.Verify navigation to Maintenance.
15.Verify navigation to Claim.
16. Verify navigation to Buzz.
12. Verify Admin module navigation.
14. Verify dropdown selection.
15. Verify admin creation
16. Verify error message when creation of admin with empty values
---


## 14. Test Execution Summary

The actual execution results are available in the generated HTML report.

| Metric | Execution Result |
|---|---|
| Total Test Cases | Refer to HTML Report |
| Passed | Refer to HTML Report |
| Failed | Refer to HTML Report |
| Skipped | Refer to HTML Report |
| Execution Report | reports/report.html |

---

## 15. Conclusion

This project demonstrates a structured approach to web application automation testing using Python, Playwright, and Pytest.

By implementing the Page Object Model, reusable methods, assertions, test execution reporting, the framework aims to improve automation maintainability, reliability, and test coverage.

The assessment focuses on validating important OrangeHRM business workflows and demonstrating practical automation testing capabilities.

**Prepared by:** Shadab Alam  
**Assessment:** SimuPhish – Sr. QA Analyst  
**Project:**Playwright python project