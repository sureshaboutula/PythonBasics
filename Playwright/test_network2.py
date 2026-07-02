import time

from playwright.sync_api import Page
from urllib3.util import url

# api call from browser (We are mocking this) -> api call contact server and return back response to bowser ->
#    -> browser uses response to generate html content
# We need to tweak the request which server receives from browser

fakePayloadOrderResponse = {"data":[],"message":"No Orders"}

def intercept_request(route):
    route.continue_(
        url = "https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6711e249ae2afd4c0b9f6fb0"
    )

def test_network_1(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)
    page.get_by_placeholder("email@example.com").fill("sureshabo@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Deva@2024")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    #time.sleep(3)
    message = page.locator(".blink_me").text_content()
    assert message == "You are not authorize to view this order"
    #print(message)
