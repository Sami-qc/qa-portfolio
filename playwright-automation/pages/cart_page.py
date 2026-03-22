class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart_items = ".cart_item"
        self.remove_button = "[data-test^='remove']"
        self.checkout_button = "[data-test='checkout']"

    def get_cart_items_count(self):
        return self.page.locator(self.cart_items).count()

    def remove_first_item(self):
        self.page.locator(self.remove_button).first.click()