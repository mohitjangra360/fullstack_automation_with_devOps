# Created by rahul at 09-09-2022
Feature: Verify Logout Page
  1.Verify user is able to see logout button after successfully login
  2.Verify user is able to logout after clicking on Logout button

  Background:
    Given open browser
    And User On Login Page
    And User login as admin

  Scenario: Verify user is able to see logout button after successfully login
    Given I would see "Logout"

  Scenario: Verify user is able to logout after clicking on Logout button
    Given click on Logout button