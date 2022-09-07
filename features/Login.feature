# Created by Mohit at 07-09-2022

Feature: Login
  Background:
    Given Open Browser

  Scenario: Verify UI of Login page
    Given I am on Login Page
    And I should see "Admin area demo"
    And I should see "Welcome, please sign in!"
    And I should see "Email:"
    And I should see "Email" input field with id
    And I should see "Password:"
    And I should see "Password" input field with id
    And I should see checkbox "RememberMe" with id
    And I should see "Remember me?"
    And I should see button "login-button" with class
    And I should see "Defaults for admin area"
    And Close Browser

  Scenario Outline: Verify login
    Given I am on Login Page
    When I set field value "<username>" and "<password>"
    Examples:
      | username | password |
      | @yourstore.com | admin |
      |admin@yourstore.com |fgjdsbf|
      |admin@yourstore.com | admin |





