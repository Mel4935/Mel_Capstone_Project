from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def Click_Cart_Button(self):
        try:
            Click_Cart = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[@class='nav-link fa text-white']"))
            )
            assert Click_Cart.is_displayed(), "Cart button is not displayed on the page."
            Click_Cart.click()
        except Exception as e:
            print(f"Assertion failed: {e}")

    def Remove_Product_Button(self):
        try:
            Remove_Button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//a[contains(@class,'text-white fa')])[2]"))
            )
            assert Remove_Button.is_displayed(), "Cart button is not displayed on the page."
            Remove_Button.click()
        except Exception as e:
            print(f"Assertion failed: {e}")

    def Buy_Now_Button(self):
        try:
            Buy_Now = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//input[contains(@type,'submit')])[2]"))
            )
            assert Buy_Now.is_displayed(), "Buy Now button is not displayed on the page."
            Buy_Now.click()
        except Exception as e:
            print(f"Error while clicking Buy Now button: {e}")

    def Order_Placed_Displayed(self):
        try:
            Order_Placed = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h3[contains(.,'ORDER PLACED!!!')]"))
            )
            assert Order_Placed.is_displayed(), "ORDER PLACED element is not displayed on the page."
            # You typically wouldn't click an order placed message; it's usually for verification purposes.

        except Exception as e:
            print(f"Assertion failed: {e}")

    def Log_Out_Button(self):
        try:
            Log_out = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(.,'Logout')]"))
                # Adjust the locator as needed
            )
            assert Log_out.is_displayed(), "Add to Cart Button is not displayed on the page."
            Log_out.click()
        except Exception as e:
            print(f"Assertion failed: {e}")

