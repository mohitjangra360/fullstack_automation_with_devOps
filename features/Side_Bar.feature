# Created by Mohit at 08-09-2022
Feature: Side Bar
  1. Verify Side Menu Bar UI
  Background:
    Given Open Browser
    And I am on Login Page
    And I login as admin

  Scenario: Verify Side Menu Bar UI
    Given I should see logo
    And I should see search box
    And I should see all side menu item is visible and clickable

    Scenario: Select Any Value From Menu Item
      Given I Select " Products" from "Catalog"
      And I goto Reports >> Customer reports >> Customers by order total
