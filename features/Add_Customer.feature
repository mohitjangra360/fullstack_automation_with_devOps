# Created by Mohit at 15-09-2022
Feature: Add Customer >> Customer
  Background:
    Given Open Browser
    And User On Login Page
    And User login as admin
    And I click on Customers
    And I select Customer under Customer Menu Item

    @SB_01
  Scenario: Verify user able to add new customer
      Given Verify add new button
      Given I click on add new button
      And I set Email
      And I set Password "1234"
      And I set First name as "XYz"
      And I set Last name as "gfd"
      And I wait 10 seconds
      And I select gender as "Male"

