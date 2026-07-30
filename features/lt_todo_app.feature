Feature: Test Simple Form Demo

  Scenario: Verify Simple Form Demo
    Given I open the Simple Form Demo page
    When I enter a message
    And I click the Show Message button
    Then I should see the entered message