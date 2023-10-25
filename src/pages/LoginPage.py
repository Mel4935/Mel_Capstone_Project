from selenium.webdriver.common.by import By   #  used to specify the method by which you want to locate HTML elements, such as by ID, name, XPath, CSS selector, etc.
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_LoginButton(self):
        try:
            login_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='Login']"))
            )
            assert login_button.is_displayed(), "Login button is not displayed on the page."

            # If the login button is present and visible, click it
            login_button.click()

        except Exception as e:
            print(f"Assertion failed: {e}")


    def enter_userId(self):
        try:
            User_Id = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='userid']"))
            )
            assert User_Id.is_displayed(), "User_Id is not displayed on the page."
            User_Id.send_keys("2972")

        except Exception as e:
            print(f"Assertion failed: {e}")

    def Final_LoginButton(self):
        try:
            Last_loginbutton = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='Login']"))
            )
            assert Last_loginbutton.is_displayed(), "Last login_button is not displayed on the page."

            # If the login button is present and visible, click it
            Last_loginbutton.click()

        except Exception as e:
            print(f"Assertion failed: {e}")