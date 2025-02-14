
# Book Cart API Automation

This repository contains automation tests for the Contact List Application.

Website: https://thinking-tester-contact-list.herokuapp.com/contactList

API Documentation: https://documenter.getpostman.com/view/4012288/TzK2bEa8#9b089533-70be-4845-afc0-95b0d3011d73

## Documentation

You can find the full documentation (Test Cases) for this project [here](https://github.com/Hadzee/Contact-List_Automation/tree/master/Documentation).

## Getting Started

This project uses Python and Playwright to automate the UI and API testing of the Contact List Application. Below are the steps to set up the environment and run the automated tests.

### Prerequisites

**Python 3.x**: This project requires Python 3.7 or higher. You can download and install Python from the official website: [Python Downloads](https://www.python.org/downloads/).

**Playwright**: The Playwright library for Python is used for browser automation. To install Playwright, use the following command:
`pip install playwright`

Additionally, you will need to install the necessary browser binaries using:
`python -m playwright install`

**pytest**: You will also need to install `pytest` for running tests. Use the following command to install it:
`pip install pytest`

## Running the Automated Tests

Once the environment is set up, you can run the Playwright tests using `pytest`.

### Running All Tests

To run all the tests, simply execute the following command in the project root directory:
`pytest`

This will discover and run all the test cases in the tests/ folder.

#### Running Specific Tests

If you want to run a specific test file, for example, test_add_contact.py, you can use the following command:
`pytest tests/ui/test_add_contact.py`

This will run only the tests in the `test_add_contact.py` file.

#### Running Tests in Headless Mode (Optional)

Playwright tests are run in headless mode by default, but you can run them with a visible browser by modifying the test configuration or using the `--headed` option:
`pytest --headed`

## Conclusion

This concludes the documentation for setting up and running the automated tests for the Contact List Application. Follow the steps above to get started with testing the application.