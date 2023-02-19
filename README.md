# Selenium Tests using Pytest for demoblaze.com

## Project Contents

### POM

Contains Page Object Model for each Screen used for Testing as following:
 - `GenericPage.py` for initiating driver and multiple used methods  
 - `MainPage.py` for locators and action of MainPage
 - `RegisterPage.py` for locators and action of RegisterPage
 - `LoginPage.py` for locators and action of LoginPage
 - `Categories.py` for locators and action of CategoriesPage
 - `CartPage.py` for locators and action of CartPage

### Workers

- `BlazeWorker.py` Worker method (Similar to Step definition in BDD)
- `helper_methods.py` helper methods that used for facilitating workers and Tests

### `constants.py`
All constant variables are used globally


### Tests

Contain test classes have multiple test_ executable methods:
- `test_user_scenarios.py` test methods for signup and login scenarios
- `test_category_items.py` test methods for checking items in categories
- `test_cart_checkout.py` test methods for add rand item to cart, delete items and complete purchasing order
- `conftest.py` contains fixtures and setup method for handling test_setup, test_teardown and logging

### Setup

Run pip install -r requirements.txt for install pipenv libraries in requirements.txt


### Execution

Using Terminal in Project Root Dir. Following is example:

- `python3 -m pytest --disable-pytest-warnings --show-capture=all -s -v --log-cli-level=INFO -m "signup_login" ./Tests/`
- `python3 -m pytest --disable-pytest-warnings --show-capture=all -s -v --log-cli-level=INFO -m "categories" ./Tests/`
- `python3 -m pytest --disable-pytest-warnings --show-capture=all -s -v --log-cli-level=INFO -m "add_delete_rand_item" ./Tests/`
- `python3 -m pytest --disable-pytest-warnings --show-capture=all -s -v --log-cli-level=INFO -m "complete_checkout" ./Tests/`

### Notes:

Feel free to change test case by marker name. Available markers are: `signup_login`, `categories`, `add_delete_rand_item` and `complete_checkout`
Arguments can be found in test_ methods and in `conftest.py` file

### Dockerising

Please run following on Project Root directory for running solution on Docker

- `docker build -t mosedky:qpros_task .`
- `docker run --name=mosedky --network=host -d mosedky:qpros_task `
- `sudo docker exec <container_id> python3 -m pytest --disable-pytest-warnings --show-capture=all -s -v --log-cli-level=INFO -m "complete_checkout" ./Tests/` or interested script from the above-mentioned Test Cases

### E2E Test Cases

- Check signup scenario
- Check Login scenario
- Check Categories from list
- Check Items in each category
- Check add random item to the cart
- Check add and delete random item from the cart
- Check Complete purchasing Order