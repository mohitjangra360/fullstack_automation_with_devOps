Feature: Test Login
  Background:
    Given Open Browser

  @smoke
  Scenario: Verify UI of Login page
    Given User On Login Page
    And Close Browser
