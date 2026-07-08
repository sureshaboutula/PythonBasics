import pytest
from pip._internal.cli import parser
from pytest_bdd import given, when, then, parsers, scenarios

from conftest import user_credentials
from pageObjects.login import LoginPage
from utils.apiBaseFramework import APIUtils

scenarios('features/orderTransaction.feature')

@pytest.fixture
def shared_data():
    return {}

@given(parsers.parse('place the item order with {username} and {password}'))
def place_item_order(playwright,  username, password, shared_data):
    user_credentials = {"userEmail": username, "userPassword": password}
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright, user_credentials)
    shared_data["order_id"] = orderId

@given('the user is on landing page')
def user_on_landing_page(browser_instance, shared_data):
    loginPage = LoginPage(browser_instance)
    loginPage.navigate()
    shared_data["login_page"] = loginPage

@when(parsers.parse('I login to portal with {username} and {password}'))
def login_to_portal(username, password, shared_data):
    loginPage = shared_data["login_page"]
    dashboardPage = loginPage.login(username, password)
    shared_data["dashboard_page"] = dashboardPage

@when('Navigate to orders page')
def navigate_to_orders_page(shared_data):
    dashboardPage = shared_data["dashboard_page"]
    orderHistoryPage = dashboardPage.selectOrderNavLink()
    shared_data["orderHistory_page"] = orderHistoryPage



@when('Select the orderId')
def select_orderId(shared_data):
    orderHistoryPage = shared_data["orderHistory_page"]
    orderId = shared_data["order_id"]
    orderDetailsPage = orderHistoryPage.selectOrder(orderId)
    shared_data["order_details_page"] = orderDetailsPage

@then('order message is successfully displayed')
def order_message(browser_instance, shared_data):
    orderDetailsPage = shared_data["order_details_page"]
    orderDetailsPage.verifyOrderMessage()