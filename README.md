# Automated Testing Project

This project is designed for automated testing using Playwright and Pytest frameworks. It is architecturally aligned with the JS Playwright and Aquality frameworks.

## Project Structure

```
├── .env.example            # Template for environment variables (secrets)
├── configs/                # Configuration files (settings.py, test_data.json)
├── framework/              # Core framework components
│   ├── logger/             # Custom logging implementation
│   ├── ui/                 # UI components
│   │   ├── browser/        # Browser and Window management
│   │   ├── constants/      # Timeouts, element states, etc.
│   │   ├── decorators/     # @step and @action decorators
│   │   ├── elements/       # UI element wrappers (Button, TextBox, etc.)
│   │   └── pages/          # BasePage class
│   └── utils/              # Utilities (EnvProvider, ConfigParser)
├── pages/                  # Application-specific Page Objects
├── tests/                  # Application-specific Test Scripts
├── conftest.py             # Pytest fixtures and browser initialization
└── pytest.ini              # Pytest configuration and markers
```

## Installing Dependencies

To get started, install the necessary dependencies by running command:

```sh
pip install -r requirements.txt
```

## Environment Setup (Secrets Management)

Before running the tests for the first time, you must configure your local environment:
1. Locate the `.env.example` file in the root directory.
2. Duplicate this file and rename the copy to `.env` (this file is ignored by Git).
3. Open your new `.env` file and populate it with the actual credentials.

If you forget to set this up, the framework's `EnvProvider` will explicitly halt test execution and warn you.

## Running Tests with Markers

You can run tests using markers with the `-m` flag. For example, to run the demo test:

```sh
pytest -m demo
```

For more details of running tests with Pytest, see [Running Tests with Pytest](https://docs.pytest.org/en/latest/how-to/usage.html).

## Running Tests with different options

To run tests with different configurations, such as specific browsers or in headless mode, use the `--browser` and `--headless` flags. By default, headless mode is disabled (False):

```sh
pytest --browser=firefox --headless
```

## Useful Links

- [Pytest Documentation](https://docs.pytest.org/en/latest/)
- [Running Tests with Pytest](https://docs.pytest.org/en/latest/how-to/usage.html)

## Unit 4 Practice Task

Run the Unit 4 suite in Chromium:

```sh
pytest -m unit_4 --browser=chromium
```

Run it in headless mode:

```sh
pytest -m unit_4 --browser=chromium --headless
```
