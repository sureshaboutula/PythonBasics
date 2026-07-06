from pageObjects.orderHistory import OrderHistoryPage


class Dashboard:

    def __init__(self, page):
        self.page = page


    def selectOrderNavLink(self):
        self.page.get_by_role("button", name="ORDERS").click()
        ordersHistoryPage = OrderHistoryPage(self.page)
        return ordersHistoryPage