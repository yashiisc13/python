from amazon.Pages.pages import HomePage, ProductListPage, ProductPage, CartPage, Windows
from log import logs

logs()

class TestWebsite(object):
    """"test class"""

    def test_main(self, mydriver, website, category, text, product_link, product, quantity):

        driver = mydriver
        driver.get(website)

        Windows(driver)
        HomePage(driver).search_product(category, text)
        ProductListPage(driver).choose_product(product_link)
        Windows(driver).switch_window()
        ProductPage(driver).add_to_cart()
        HomePage(driver).go_to_cart()
        cart_list = CartPage(driver).check_cart(product, quantity)
        assert cart_list[0] == "War And Peace"
        assert cart_list[1] == "1"

        driver.quit()
