from playwright.sync_api import Playwright

ordersPayload = {"orders": [{"country": "India", "productOrderedId": "6960eae1c941646b7a8b3ed3"}]}
tokenPayload = {
    "userEmail": "sureshabo@gmail.com",
    "userPassword": "Deva@2024"
}

class APIUtils:

    def getToken(self, playwright:Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        response = api_request_context.post(
            "/api/ecom/auth/login",
            data=tokenPayload
        )
        assert response.ok
        responseBody = response.json()
        return responseBody["token"]

    def createOrder(self, playwright:Playwright):
        token = self.getToken(playwright)
        api_request_context = playwright.request.new_context(
            base_url="https://rahulshettyacademy.com"
        )
        response = api_request_context.post(
            "/api/ecom/order/create-order",
            data= ordersPayload,
            headers={
                "Content-Type": "application/json",
                "Authorization":token
            }
        )
        #print(response.json())
        response_body = response.json()
        orderId = response_body["orders"][0]
        return orderId