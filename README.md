# Playwright - Pytest

## Project Description

Playwright - Pytest is a project that utilizes the Playwright pytest framework to perform end-to-end (e2e) automated testing. The project is designed to cover a variety of test cases, leveraging both the `expect` and `assert` methods for verification. It integrates with GitHub Actions for continuous integration and generates Allure reports for test result visualization.

## How to Install and Run the Project

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/playwright-pytest.git
   cd pytest
   ```

2. Install the necessary dependencies:

   ```bash
    python -m pip install --upgrade pip
    pip install pipenv
    pipenv install --dev
    pipenv run pip install pytest-playwright
    pipenv run playwright install chromium
   ```

3. To run the tests:

   ```bash
   pytest
   pytest --browser chromium --headed  # Run with visible browser
   ```

4. To generate the Allure report:
   ```bash
   pytest --alluredir=./reports --clean-alluredir
   allure serve reports
   ```

## How to Use the Project

- The project includes automated tests that cover various parts of the application. You can run all tests or select specific tests to run based on the markers defined in the `markers` section.
- The tests are written using the Playwright framework combined with Pytest, and they are organized based on different functionalities like login, contact forms, and signup.
- The test cases are also marked for better organization. The following markers are used:

  - **login**: Login and signup tests
  - **product**: Product and search tests
  - **other**: Contact, subscription, and test cases tests

- You can run tests based on these markers for more targeted test execution:

  ```bash
  pytest -m <marker_name>
  ```

- You can add or modify test cases in the `tests` directory, and customize the framework to suit your needs.

## License

This project is for training purposes and does not require a license.
