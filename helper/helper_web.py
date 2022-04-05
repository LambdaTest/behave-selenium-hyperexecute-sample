from selenium import webdriver
from helper.helper_base import HelperFunc
import os

caps = {}

def get_browser(browser, browser_version):
    user_name = os.environ.get("LT_USERNAME")
    access_key = os.environ.get("LT_ACCESS_KEY")

    caps['name'] = "[LambdaTest] [Behave] Testing using Behave and Selenium"
    caps['build'] = "[LambdaTest] [Behave] Testing using Behave and Selenium"
    caps['browserName'] = browser
    caps['version'] = browser_version
    caps['platform'] = os.environ.get("TARGET_OS")
    caps['network'] = True
    caps['visual'] = True
    caps['video'] = True
    caps['console'] = True
    # Accept Insecure Certs (Will not work, details at
    # https://github.com/SeleniumHQ/selenium/issues/6534#issuecomment-499961981)
    caps['acceptInsecureCerts'] = True
    # Known Issue : Selenium Remote WebDriver ignores invalid SSL certificates
    # https://github.com/SeleniumHQ/selenium/issues/6534#issuecomment-499961981
    # Even with valid SSL certificate https://www.ssllabs.com/ssltest/analyze.html?d=hub.lambdatest.com&latest, error pops
    # up
    ########## Error ################
    #HTTPSConnectionPool(host='hub.lambdatest.com', port=443): Max retries exceeded with url: /wd/hub/session (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)')))
    #HOOK-ERROR in after_all: AttributeError: 'Context' object has no attribute 'helperfunc'
    # Workaround - Disable HTTPS connection and use HTTP connection
    #remote_url = "http://" + "LT_USER_NAME" + ":" + "LT_ACCESS_KEY" \
    #            + "@hub.lambdatest.com/wd/hub"
    remote_url = "https://" + user_name + ":" + access_key + "@hub.lambdatest.com/wd/hub"
    return HelperFunc(webdriver.Remote(command_executor=remote_url, desired_capabilities=caps))
