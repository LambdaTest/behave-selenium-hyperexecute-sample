from behave import given, when, then

MESSAGE = "Welcome to TestMu AI"

@given("I open the Simple Form Demo page")
def step(context):
    context.helperfunc.open(
        "https://www.testmuai.com/selenium-playground/simple-form-demo"
    )

@when("I enter a message")
def step(context):
    context.helperfunc.find_by_id("user-message").send_keys(MESSAGE)

@when("I click the Show Message button")
def step(context):
    context.helperfunc.find_by_id("showInput").click()

@then("I should see the entered message")
def step(context):
    displayed = context.helperfunc.find_by_id("message").text
    assert displayed == MESSAGE