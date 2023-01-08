import pytest
import allure
from pages.order_page import OrderPage
from conftest import ORDERS, LINK_DZEN, LINK_BASE_PAGE, TEXT_ORDER_IS_DONE


@allure.suite('Test suite to make an order')
class TestCreateOrder:
    @allure.title('Create an order')
    @allure.description('Perform all steps to create an order from very begin to the last step')
    @pytest.mark.parametrize('order', ORDERS)
    def test_order_from_header_success(self, driver, order):

        page = OrderPage(driver)
        page.accept_cookies()
        page.click_order_button(order['by_button'])
        page.fill_customer_data(
            order['firstname'],
            order['lastname'],
            order['address'],
            order['subway_station'],
            order['phone']
        )
        page.click_button_next()
        page.fill_order_data(
            order['date'],
            order['duration'],
            order['color'],
            order['comment']
        )
        page.click_button_to_submit()
        page.click_button_confirm()
        page.verify_if_order_is_created()
        assert TEXT_ORDER_IS_DONE in page.verify_if_order_is_created()
        assert LINK_DZEN == page.verify_if_link_to_yandex_works()
        assert LINK_BASE_PAGE == page.verify_if_link_to_base_page_works()
