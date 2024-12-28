Feature: Greet the user
  To ensure the greeting function works correctly

  Scenario: Greet a specific user
    Given a user named "Alice"
    When the user is greeted
    Then the response should be "Hello, Alice!"

  Scenario: Greet with an empty name
    Given an empty name
    When the user is greeted
    Then the response should be "Hello, Guest!"
