# eCommerce_demo Playwright Automation Suite (Python)

# Features
- Automated UI tests using Python + Playwright
- Validates:
  - Z → A sorting
  - Price high → low sorting
  - Add to cart + checkout flow
  - Visual screenshot checks
  - Accessibility compliance (axe-core)

---

# Prerequisites

Before you begin, ensure that you have the following installed:

  - Python 3.10+: Download from python.org.
  - pip (Python package manager): Should come installed with Python.
  - Google Chrome (or any Playwright-supported browser): Chrome is recommended, but Playwright will work with Chromium by default.

---

# Setup Instructions

1. Clone the repository:
   First, clone the repository to your local machine:
   
        git clone https://github.com/Vijay-QC/eCommerce_demo.git
        cd eCommerce_demo
   
2. Create and Activate a Virtual Environment
It's recommended to create a virtual environment for this project to manage dependencies in isolation.

        python -m venv venv

On Windows, activate the virtual environment:

    venv\Scripts\activate

3. Install Required Dependencies
Use pip to install the necessary dependencies:

        pip install -r requirements.txt
   
This will install the required libraries, including Playwright and testing dependencies.

4. Install Playwright Browsers
Playwright needs browser binaries (Chromium, Firefox, WebKit) to run tests. Install them using:

       playwright install

This will download and install the necessary browser binaries for testing.

---

# Running the Tests Locally

1. Run Tests in Headless Mode (Default)

        pytest --html=reports/index.html

This will execute all the tests and generate an HTML report in the reports folder.

2. Run Tests in Headed Mode

       pytest --headed --html=reports/index.html

This will open the browser window while running the tests, useful for debugging.

3. Test Execution Logs/Reports
Reports: After running the tests, you can view the results in the generated HTML report (reports/index.html).

To open the report: start reports/index.html

---

# Updating the Repository

1. Commit Your Changes

       git add .
       git commit -m "Initial Commit"

2. Push Changes to GitHub

       git push -u origin main

3. Test Execution Videos
You can find the video recordings of both headless and headed test runs in the Videos/ folder. These can be useful for debugging or showcasing the tests.

Headed mode: Videos/Headed_run.mp4
Headless mode: Videos/Headless_run.mp4
