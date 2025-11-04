# E-commerce Web Application Automation Testing Framework

**Tech stack:** Python, Selenium, PyTest, Page Object Model (POM), pytest-html, webdriver-manager

## Project structure
```
Ecommerce_Automation/
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── search_page.py
│   └── cart_page.py
├── utilities/
│   ├── driver_setup.py
│   └── config_reader.py
├── tests/
│   ├── test_login.py
│   ├── test_search.py
│   └── test_add_to_cart.py
├── config/
│   └── config.ini
├── requirements.txt
├── pytest.ini
├── Jenkinsfile
└── README.md
```

## Quick start

1. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux / macOS
   venv\Scripts\activate    # Windows (PowerShell)
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run tests:
   ```bash
   pytest
   ```
4. Open the generated report:
   ```
   reports/report.html
   ```

## Notes
- `driver_setup.py` uses `webdriver-manager` to download the appropriate ChromeDriver automatically.
- `config/config.ini` contains the base URL and a sample test user. Change values as needed.
- To run in non-headless mode, set `headless = False` in `config/config.ini`.

## Jenkins
A `Jenkinsfile` is included for a simple pipeline that installs dependencies and runs the pytest suite.
