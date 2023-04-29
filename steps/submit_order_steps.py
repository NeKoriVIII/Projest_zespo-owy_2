from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By



@given('User is on main page')
def on_mainpage(context):
    context.driver = webdriver.Chrome(executable_path='C:\\TestFiles\\chromedriver.exe')
    context.driver.get('https://practicesoftwaretesting.com/#/')
    time.sleep(2)

@given('User is logged in')
def login(context):
    context.driver.find_element(By.LINK_TEXT, 'Sign in').click()
    context.driver.find_element(By.ID, 'email').send_keys('test@example.com')
    context.driver.find_element(By.ID, 'password').send_keys('qwerty')
    context.driver.find_element(By.CLASS_NAME, 'btnSubmit').click()
    context.driver.find_element(By.LINK_TEXT, 'Home').click()

@when('The user adds one product to the cart')
def add_one_prod(context):
    context.driver.find_element(By.LINK_TEXT, 'Combination Pliers').click()
    context.driver.find_element(By.ID, 'btn-add-to-cart').click()

@when('The user goes to the cart and clicks Proceed to checkout')
def go_to_cart(context):
    context.driver.find_element(By.ID, 'lblCartCount').click()
    context.driver.find_element(By.LINK_TEXT, 'Proceed to checkout').click()

@when('The user passes login verification and click Proceed to checkout')
def login_ver(context):
    context.driver.find_element(By.LINK_TEXT, 'Proceed to checkout').click()

@when('The user confirms his address and clicks Proceed to checkout')
def confirm_address(context):
    context.driver.find_element(By.LINK_TEXT, 'Proceed to checkout').click()

@when('The user is entering the payment details correctly and klick Confirm')
def paymen_details(context):
    context.driver.find_element(By.ID, 'payment-method').click()
    context.driver.find_element(By.LINK_TEXT, 'Bank Transfer').click()
    context.driver.find_element(By.ID, 'account-name').send_keys('John Smith')
    context.driver.find_element(By.ID, 'account-number').send_keys('1111 1111 1111 1111')
    context.driver.find_element(By.LINK_TEXT, 'Confirm').click()
    time.sleep(2)
    context.driver.find_element(By.LINK_TEXT, 'Confirm').click()

@then('Order placed')
def place_ordre(context):
    assert 'Thanks for your order!' in context.driver.page_source

@then('The user goes to the home page')
def go_home(context):
    context.driver.find_element(By.LINK_TEXT, 'Home').click()

@when('The user adds 17e+307 products to the cart')
def adds_17e_prods(context):
    context.driver.find_element(By.LINK_TEXT, 'Combination Pliers').click()
    context.driver.find_element(By.XPATH, '/html/body/app-root/div/app-detail/div[1]/div[2]/div[1]/input').send_keys('17e+307')
    context.driver.find_element(By.ID, 'btn-add-to-cart').click()\

@when('The user adds two different products to the cart')
def adds_two_prods(context):
    context.driver.find_element(By.LINK_TEXT, 'Combination Pliers').click()
    context.driver.find_element(By.ID, 'btn-add-to-cart').click()
    context.driver.find_element(By.LINK_TEXT, 'Home').click()
    context.driver.find_element(By.LINK_TEXT, 'Pliers').click()
    context.driver.find_element(By.ID, 'btn-add-to-cart').click()\

@when('The user adds a non-integer number products to the cart')
def adds_oneandhalf_prods(context):
    context.driver.find_element(By.LINK_TEXT, 'Combination Pliers').click()
    context.driver.find_element(By.XPATH, '/html/body/app-root/div/app-detail/div[1]/div[2]/div[1]/input').send_keys('1.5')
    context.driver.find_element(By.ID, 'btn-add-to-cart').click()

@when('The user logs out')
def logout(context):
    context.driver.find_element(By.ID, 'user-menu').click()
    context.driver.find_element(By.LINK_TEXT, 'Sign out').click()
    context.driver.find_element(By.LINK_TEXT, 'Home').click()

@when('The user logs in')
def logs_in(context):
    context.driver.find_element(By.ID, 'email').send_keys('test@example.com')
    context.driver.find_element(By.ID, 'password').send_keys('qwerty')
    context.driver.find_element(By.CLASS_NAME, 'btnSubmit').click()

@when('The user tries to log in without entering any data')
def login_without_data(context):
    context.driver.find_element(By.CLASS_NAME, 'btnSubmit').click()

@then('Order is not placed')
def order_not_placed(context):
    assert 'Email is required.' in context.driver.page_source
    assert 'Password is required..' in context.driver.page_source

@when('The user deletes his address')
def del_address(context):
    context.driver.find_element(By.ID, 'address').clear

@then('Order did not place, the address is required')
def without_address(context):
    assert 'Address is required.' in context.driver.page_source

@when('The user deletes his city')
def del_city(context):
    context.driver.find_element(By.ID, 'city').clear

@then('Order did not place, city is required')
def without_city(context):
    assert 'City is required.' in context.driver.page_source

@when('The user deletes his state')
def del_state(context):
    context.driver.find_element(By.ID, 'state').clear

@then('Order did not place, state is required')
def without_state(context):
    assert 'State is required.' in context.driver.page_source

@when('The user deletes his country')
def del_country(context):
    context.driver.find_element(By.ID, 'country').clear

@then('Order did not place, country is required')
def without_country(context):
    assert 'Country is required.' in context.driver.page_source

@when('The user deletes his postalcode')
def del_postalcode(context):
    context.driver.find_element(By.ID, 'postalcode').clear

@then('Order did not place, postalcode is required')
def without_postalcode(context):
    assert 'Postalcode is required.' in context.driver.page_source

@when('The user is entering the payment details without account name and klick Confirm')
def nonenter_accname(context):
    context.driver.find_element(By.ID, 'payment-method').click()
    context.driver.find_element(By.LINK_TEXT, 'Bank Transfer').click()
    context.driver.find_element(By.ID, 'account-number').send_keys('1111 1111 1111 1111')
    context.driver.find_element(By.LINK_TEXT, 'Confirm').click()

@then('Order did not place, account name is required.')
def without_accname(context):
    assert 'Account name is required.' in context.driver.page_source

@when('The user is entering the payment details without account number and klick Confirm')
def nonenter_accnum(context):
    context.driver.find_element(By.ID, 'payment-method').click()
    context.driver.find_element(By.LINK_TEXT, 'Bank Transfer').click()
    context.driver.find_element(By.ID, 'account-name').send_keys('John Smith')
    context.driver.find_element(By.LINK_TEXT, 'Confirm').click()

@then('Order did not place, account number is required.')
def without_accnum(context):
    assert 'Account number is required.' in context.driver.page_source

@when('The user is entering the payment details without payment-method and klick Confirm')
def nonenter_paymethod(context):
    context.driver.find_element(By.ID, 'account-name').send_keys('John Smith')
    context.driver.find_element(By.ID, 'account-number').send_keys('1111 1111 1111 1111')
    context.driver.find_element(By.LINK_TEXT, 'Confirm').click()

@then('Order did not place, payment-method is required.')
def without_paymethod(context):
    assert 'Payment-method is required.' in context.driver.page_source

@when('The user does not enter payment details and klicks Confirm')
def nonenter_paydetails(context):
    context.driver.find_element(By.LINK_TEXT, 'Confirm').click()

@then('Order did not place, payment details are required.')
def without_paydetails(context):
    assert 'Account name is required.' in context.driver.page_source
    assert 'Account number is required.' in context.driver.page_source
    assert 'Payment-method is required.' in context.driver.page_source

@then('The User closes the browser')
def close_browser(context):
    context.driver.quit()
