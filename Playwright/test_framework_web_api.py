import json
import time

import pytest
from playwright.sync_api import Playwright, expect

from pageObjects.login import LoginPage
from utils.apiBaseFramework import APIUtils

# file_path = Path("data/credentials.json")
# print("cwd:", os.getcwd())
# print("file_path:", file_path)
# print("absolute:", file_path.resolve())
# print("exists:", file_path.exists())
# print("is_file:", file_path.is_file())
# Access user credentials from data/credentials.json
with open("data/credentials.json", 'r') as f:
    test_data = json.load(f)
    # print(test_data["user_credentials"][0])
    user_credentials_list = test_data["user_credentials"]


@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_e2e_web_api(playwright:Playwright, browser_instance, user_credentials):
    userName = user_credentials["userEmail"]
    userPassword = user_credentials["userPassword"]

    # Below code is handled through fixture - browser_instance
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()

    #print(user_credentials["userEmail"])
    # Create Order -> orderId
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright, user_credentials)

    #Login
    loginPage = LoginPage(browser_instance)
    loginPage.navigate()
    #page.goto("https://rahulshettyacademy.com/client")

    dashboardPage = loginPage.login(userName, userPassword)
    # page.get_by_placeholder("email@example.com").fill(userName)
    # page.get_by_placeholder("enter your passsword").fill(userPassword)
    # page.get_by_role("button", name="Login").click()

    # Orders history page -> order is present
    #Dashboard Page
    #dashboardPage = Dashboard(page)
    orderHistoryPage = dashboardPage.selectOrderNavLink()
    orderDetailsPage = orderHistoryPage.selectOrder(orderId)
    # page.get_by_role("button", name="ORDERS").click()
    #expect(page.locator("tr").filter(has_text=orderId)).to_be_visible()

    # row = page.locator("tr").filter(has_text=orderId)
    # row.get_by_role("button", name="View").click()
    #orderDetailsPage = orderHistoryPage.selectOrder(orderId)
    orderDetailsPage.verifyOrderMessage()
    #expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
    #time.sleep(10)
    #context.close( )
