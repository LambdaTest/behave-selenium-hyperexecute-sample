from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from behave import given, when, then
import urllib3

urllib3.disable_warnings()

@given('I go to Selenium playground home page')
def step(context):
    context.helperfunc.open('https://www.lambdatest.com/selenium-playground/')
    context.helperfunc.maximize()

@then('I Click on Input Form Link')
def click_on_submit_link(context):
    time.sleep(3)
    element = context.helperfunc.find_by_xpath("//a[.='Input Form Submit']")
    element.click()

@then('I enter items in the form')
def enter_items_in_form(context):
    name = context.helperfunc.find_by_xpath("//input[@id='name']")
    name.send_keys("Testing")

   email_address = context.helperfunc.find_by_css_selector("#inputEmail4")
   email_address.send_keys("testing@testing.com")

    password = context.helperfunc.find_by_xpath("//input[@name='password']")
    password.send_keys("password")

    company = context.helperfunc.find_by_css_selector("#company")
    company.send_keys("LambdaTest")

    website = context.helperfunc.find_by_css_selector("#websitename")
    website.send_keys("https://wwww.lambdatest.com")

    country_dropdown = Select(context.helperfunc.find_by_xpath("//select[@name='country']"))
    country_dropdown.select_by_visible_text("United States")

    city = context.helperfunc.find_by_xpath("//input[@id='inputCity']")
    city.send_keys("San Jose")

    address1 = context.helperfunc.find_by_css_selector("[placeholder='Address 1']")
    address1.send_keys("Googleplex, 1600 Amphitheatre Pkwy")

    address2 = context.helperfunc.find_by_css_selector("[placeholder='Address 2']")
    address2.send_keys("Mountain View, CA 94043")

    state = context.helperfunc.find_by_css_selector("#inputState")
    state.send_keys("California")

    zipcode = context.helperfunc.find_by_css_selector("#inputZip")
    zipcode.send_keys("94088")

@when('I click submit button')
def click_on_submit_button(context):
    # Click on the Submit button
    submit_button = context.helperfunc.find_by_css_selector(".btn")
    submit_button.click()

@then('I should verify if form submission was successful')
def verify_submit_operation(context):
    # Assert if the page contains a certain text
        assert context.helperfunc.find_on_page("Thanks for contacting us, we will get back to you shortly")

        time.sleep(10)
        print("Input Form Demo complete")
