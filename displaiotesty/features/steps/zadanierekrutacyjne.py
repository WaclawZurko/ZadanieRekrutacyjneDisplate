from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC	
from time import sleep


COOKIES_BUTTON = '//*[@id="cookie-alert-container"]/div/button'
FIRST_PRODUCT_HOMEPAGE = '//*[@id="homepage-feed"]/div/div[1]/div/div/div/div/div/div[1]'
BREADCRUMBS_PRODUCTPAGE = '//*[@id="react-product-page"]/div/div[1]/div[1]'
FRAME_4 = '//*[@id="react-product-page"]/div/div[1]/section/div[2]/div[2]/div[2]/div[2]/label[4]/div'
PRODUCT_FINISH = '//*[@id="react-product-page"]/div/div[1]/section/div[2]/div[2]/div[1]/div[2]/label[2]/span[1]'
ADD_TO_CART_BTN = '//*[@id="react-product-page"]/div/div[1]/section/div[2]/div[3]/div[1]/button'
PROCEED_TO_CART = '//*[@id="react-product-page"]/div/div[1]/section/div/div/a'
CART_HEADER = '//*[@id="cart-container"]/form/div[1]/div[1]/h1'
PRICE_CART_SUMMARY = '//*[@id="cart-total"]'
USA = '//*[@id="select-country"]/div[2]/div[3]/div/div[41]'
SUBTOTAL_PRICE = '//*[@id="cart-container"]/form/div[1]/div[1]/div[2]/div[2]/div/div[3]/div/span[2]'
SELECTED_COUNTRY = '//*[@id="select-country"]/div[1]'
PROMO_CODE_TOPBAR = '//*[@id="main-menu"]/nav/div[1]/div/div[2]/span[2]/strong[3]'
OPEN_DISCOUNT_INPUT = '//*[@id="cart-container"]/form/div[2]/div[1]/div[6]/div/div[1]'
OLD_SUBTOTAL = '//*[@id="cart-container"]/form/div[1]/div[1]/div[2]/div[2]/div/div[3]/div/span[2]'
NEW_SUBTOTAL = '//*[@id="cart-container"]/form/div[1]/div[1]/div[2]/div[2]/div/div[3]/div/span[3]'


@given('we start at homepage')
def open_homepage(context):
	context.driver = webdriver.Chrome()
	context.driver.get('http://displate.com')
	context.driver.maximize_window()
	context.driver.find_element_by_xpath(COOKIES_BUTTON).click()

@when('we click at first product')
def click_at_first_product(context):
	context.driver.execute_script("window.scrollTo(0, 1080)") 
	context.driver.find_element_by_xpath(FIRST_PRODUCT_HOMEPAGE).click()

@then('we should land on product page')
def assert_product_page(context):
	assert context.driver.find_element_by_xpath(BREADCRUMBS_PRODUCTPAGE).is_displayed()

@when('we select product frame')
def select_product_frame(context):
	context.driver.find_element_by_xpath(FRAME_4).click()

@when('we select product finish')
def select_product_finish(context):
	context.driver.find_element_by_xpath(PRODUCT_FINISH).click()

@when('we add product to cart')
def add_product_to_cart(context):
	WebDriverWait(context.driver, 15).until(EC.visibility_of_element_located((By.XPATH, ADD_TO_CART_BTN)))
	context.driver.find_element_by_xpath(ADD_TO_CART_BTN).click()

@then('we should proceed to cart')
def proceed_to_cart(context):
	WebDriverWait(context.driver, 15).until(EC.visibility_of_element_located((By.XPATH, PROCEED_TO_CART)))
	context.driver.find_element_by_xpath(PROCEED_TO_CART).click()


@then('we should land on cart page')
def assert_cart_page(context):
	WebDriverWait(context.driver, 15).until(EC.visibility_of_element_located((By.XPATH, CART_HEADER)))
	assert context.driver.find_element_by_xpath(CART_HEADER).is_displayed()

@then('we should check if price is fine')
def assert_price_is_in_range(context):
	# nie bardzo wiem co autor mial na mysli, wiec zrobilem zwykle porownanie
	price = context.driver.find_element_by_xpath(PRICE_CART_SUMMARY).text
	assert int(price[1:]) > 35

@when('we change country to united states')
def change_country_to_usa(context):
	context.driver.find_element_by_id('select-country').click()
	element = context.driver.find_element_by_xpath(USA)
	element.location_once_scrolled_into_view
	WebDriverWait(context.driver, 15).until(EC.visibility_of_element_located((By.XPATH, USA)))
	context.driver.find_element_by_xpath(USA).click()

@then('we should see proper country')
def assert_country_is_usa(context):
	sleep(1) # tak wiemy, ze sleep to zla praktyka ale nie bardzo wiem jak to inaczej obejsc
	context.driver.refresh()
	sleep(1)
	context.driver.execute_script("window.scrollTo(0, 0)") 
	price = context.driver.find_element_by_xpath(SUBTOTAL_PRICE).text
	assert str(price[:1]) == "$"
	assert context.driver.find_element_by_xpath(SELECTED_COUNTRY).text == "United States"

@when('we use promo code from topbar')
def use_topbar_promocode(context):
	promocode = context.driver.find_element_by_xpath(PROMO_CODE_TOPBAR).text
	context.driver.find_element_by_xpath(OPEN_DISCOUNT_INPUT).click()
	promocode_input = context.driver.find_element_by_id('discount-code')
	promocode_input.clear()
	promocode_input.send_keys(promocode)
	context.driver.find_element_by_id('discount-apply').click()

@then('we should see price has changed')
def assert_price_has_changed(context):
	WebDriverWait(context.driver, 15).until(EC.visibility_of_element_located((By.XPATH, NEW_SUBTOTAL)))
	assert context.driver.find_element_by_xpath(OLD_SUBTOTAL).is_displayed()
	assert context.driver.find_element_by_xpath(NEW_SUBTOTAL).is_displayed()
