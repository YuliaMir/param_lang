from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_user_should_see_addtobasket_button(browser):
    browser.get(link)
    time.sleep(30)
    assert browser.find_element_by_css_selector("#add_to_basket_form"), "No add to basket button on the page"


