from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys
import time
from behave import given, when, then
import urllib3

urllib3.disable_warnings()

@given('I go to 4davanceboy to add item')
def step(context):
    context.helperfunc.open('https://lambdatest.github.io/sample-todo-app/')
    context.helperfunc.maximize()

@then('I Click on first checkbox and second checkbox')
def click_on_checkbox_one(context):
    context.helperfunc.find_by_name('li1').click()
    context.helperfunc.find_by_name('li2').click()

@when('I enter item to add')
def enter_item_name(context):
    context.helperfunc.find_by_id('sampletodotext').send_keys("Yey, Let's add it to list")

@when('I click add button')
def click_on_add_button(context):
    context.helperfunc.find_by_id('addbutton').click()

@then('I should verify the added item')
def see_login_message(context):
    added_item = context.helperfunc.find_by_xpath("//span[@class='done-false']").text

    time.sleep(10)

    if added_item in "Yey, Let's add it to list":
        return True
    else:
        return False
