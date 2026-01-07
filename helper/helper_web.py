from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from helper.helper_base import HelperFunc
import os


def get_browser(browser, browser_version):
    user_name = os.environ.get("LT_USERNAME")
    access_key = os.environ.get("LT_ACCESS_KEY")

    # LambdaTest specific capabilities
    lt_options = {
        'name': "[LambdaTest] [Behave] Testing using Behave and Selenium",
        'build': "[LambdaTest] [Behave] Testing using Behave and Selenium",
        'platformName': os.environ.get("TARGET_OS"),
        'network': True,
        'visual': True,
        'video': True,
        'console': True,
    }

    # Select browser-specific options
    browser_lower = browser.lower()
    if browser_lower == "chrome":
        options = ChromeOptions()
    elif browser_lower == "firefox":
        options = FirefoxOptions()
    elif browser_lower in ["edge", "microsoftedge"]:
        options = EdgeOptions()
    elif browser_lower == "safari":
        options = SafariOptions()
    else:
        # Default to Chrome options
        options = ChromeOptions()

    # Set browser version
    options.browser_version = browser_version

    # Set LambdaTest capabilities using the LT:Options key
    options.set_capability('LT:Options', lt_options)

    remote_url = "https://" + user_name + ":" + access_key + "@hub.lambdatest.com/wd/hub"
    return HelperFunc(webdriver.Remote(command_executor=remote_url, options=options))
