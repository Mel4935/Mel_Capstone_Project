from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def search_bar(self):
        try:
            Search_Box = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='search']"))
            )
            assert Search_Box.is_displayed(), "Search Box is not displayed on the page."
            Search_Box.send_keys("PC")  # Input text into the search box

        except Exception as e:
            print(f"Error: {e}")

    def Show_Amount_Entries(self):

        try:
            Show_Entries = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//select[contains(@name,'length')]"))
            )
            assert Show_Entries.is_displayed(), "Show Entries dropdown is not displayed on the page."

            # Use the Select class to interact with the dropdown
            select = Select(Show_Entries)
            select.select_by_value("100")  # Select the wanted option by its value

        except Exception as e:
            print(f"Assertion failed: {e}")
