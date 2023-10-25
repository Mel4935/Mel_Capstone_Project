from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select  # Import the Select class


class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    def quick_view_button(self):
        try:
            Quick_View = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(@data-target,'10')]"))
            )
            assert Quick_View.is_displayed(), "QuickView is not displayed on the page."
            Quick_View.click()
        except Exception as e:
            print(f"Assertion failed: {e}")

    def select_quantity(self, quantity):
        try:
            quantity_dropdown = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//select[@name='quantity'])[9]"))
                # Adjust the locator as needed
            )
            assert quantity_dropdown.is_displayed(), "Quantity dropdown is not displayed on the page."

            # Use the Select class to interact with the dropdown
            select = Select(quantity_dropdown)
            select.select_by_value("2")  # Use "2" if it's one of the values in the dropdown

            return select.first_selected_option.text  # Return the selected quantity option
        except Exception as e:
            print(f"Error: {e}")
            return None

    def add_to_cart_button(self):
        try:
            Add_Cart = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//button[contains(.,'Add to cart')])[18]"))
            )
            assert Add_Cart.is_displayed(), "Add to Cart Button is not displayed on the page."
            Add_Cart.click()

        except Exception as e:
            print(f"Assertion failed: {e}")

    def add_more_to_cart(self):
        try:
            Add_More_Cart = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[@type='submit'][1]"))
                # Adjust the locator as needed
            )
            assert Add_More_Cart.is_displayed(), "Add to Cart Button is not displayed on the page."
            Add_More_Cart.click()
        except Exception as e:
            print(f"Assertion failed: {e}")

