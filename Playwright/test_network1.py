from playwright.sync_api import Page

# api call from browser -> api call contact server and return back response to bowser(we are mocking this) ->
#    -> browser uses response to generate html content
# We need to tweak the response which server sends to browser

fakePayloadOrderResponse = {"data":[],"message":"No Orders"}

def intercept_response(route):
    route.fulfill(
        json = fakePayloadOrderResponse
    )

def test_network_1(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.get_by_placeholder("email@example.com").fill("sureshabo@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Deva@2024")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    order_text =  page.locator(".mt-4").text_content()
    assert order_text == " You have No Orders to show at this time. Please Visit Back Us "
    #print(order_text)