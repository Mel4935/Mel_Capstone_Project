import time
from selenium import webdriver
from src.pages.LandingPage import LandingPage
from src.pages.RegPage import RegPage
from src.pages.LoginPage import LoginPage
from src.pages.ProductPages import ProductPage
from src.pages.OrderPage import OrderPage
from src.pages.CartPage import CartPage


driver = webdriver.Chrome()
driver.get('http://shop.icraftsoft.net:8095/')

# Landing Page
lp = LandingPage(driver)
lp.click_login()
time.sleep(4)


# Register username and password
rg = RegPage(driver)
rg.getUsername()
rg.getEmail()
rg.getButton()
time.sleep(4)

# Click Login
cl = LoginPage(driver)
cl.click_LoginButton()
time.sleep(4)

# Enter User_Id
ui = LoginPage(driver)
ui.enter_userId()
time.sleep(4)

# Final login button
flb = LoginPage(driver)
flb.Final_LoginButton()
time.sleep(7)

# Product Page
# Search Bar
sb = ProductPage(driver)
sb.search_bar()
time.sleep(4)

# Show Entries
se = ProductPage(driver)
se.Show_Amount_Entries()
time.sleep(4)

# Quick View of the product
qv = OrderPage(driver)
qv.quick_view_button()
time.sleep(4)

# Choose Quantity
q = OrderPage(driver)
q.select_quantity(2)
time.sleep(4)

# Add to Cart
Atc = OrderPage(driver)
Atc.add_to_cart_button()
time.sleep(4)

# Add more to Cart
amt = OrderPage(driver)
amt.add_more_to_cart()
time.sleep(4)

# Open Cart Page
cp = CartPage(driver)
cp.Click_Cart_Button()
time.sleep(4)

# Remove item from cart
rp = CartPage(driver)
rp.Remove_Product_Button()
time.sleep(4)

# Buy Now Button
bn = CartPage(driver)
bn.Buy_Now_Button()
time.sleep(4)

# Order Placed Text Displayed
op = CartPage(driver)
op.Order_Placed_Displayed()
time.sleep(4)

# Log out Button
lo = CartPage(driver)
lo.Log_Out_Button()
time.sleep(4)
