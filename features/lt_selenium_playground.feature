Feature: Test run on LambdaTest Selenium Playground

Scenario: Test Input Form on Playground
  Given I go to Selenium playground home page
  Then I Click on Input Form Link
  Then I enter items in the form
  When I click submit button
  Then I should verify if form submission was successful