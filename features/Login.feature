# Created by Mohit at 08-09-2022
  @Login @Ibran
Feature: Login
  1. Verify Login Page UI
  2. Verify user login with valid username & password
  3. Verify user loign with invalid username & valid password
  4. Verify user login with valid username & invalid password

  Background:
    Given Open Browser
    And I am On Login Page

    @LP_01
  Scenario: Verify Login Page UI
      Given I should see "Admin area demo"
      And I should see "Welcome, please sign in!"
      And I should see "Email:"
      And I should see "Password:"
      And I should see "Remember me?"
      And I should see "Log in"
      And I should see "Defaults for admin area"
      And I should see "Email" input field by id
      And I should see "Password" input field by id

   Scenario Outline: Verify user able to login with valid or invalid data
     Given I set field value "<username>" and "<password>"
     Examples:
       | username | password |
       | admin@yourstore.com | ngjkdfngkjdf|
       |admin@yourstore.comfjdgdkj | admin |
       |admin@yourstore.com        | admin |
     And I should see "Wrong email"


      