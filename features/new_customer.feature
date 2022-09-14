# Created by Ekta at 08-09-2022
  @New_customer
Feature: New customer
  1. Verify user must be able to see new customer box with label
  2. Verify user must be able to see( + ) Expand new customer Button Is Visible
  3. Click On ( + ) Expand Button
  4. Verify user must be able to see new customer List Item Table Is Visible
  5. Verify user must be able to see Refresh Button Is Visible
  Background:
    Given Open Browser
    And User On Login Page

    @D_NC_01 @smoke
  Scenario:Verify user must be able to see new customer box with label
#      Given I should see "New customers"
      Given I wait 4 seconds
#      Then I should see "fas fa-plus"
      And I should see new_customer expand button
      And  I should see "week"
      And  I should see "month"
      And  I should see "year"
      And I should see "graph"




