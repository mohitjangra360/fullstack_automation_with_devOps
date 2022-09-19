# Created by Mohit at 15-09-2022
Feature: Add Customer >> Customer
  Background:
    Given Open Browser
     And I am on Login Page
    And I login as admin
    And I click on Customers
    And I select Customer under Customer Menu Item

    @SB_01
  Scenario: Verify user able to add new customer
    Given I click on add new button
      And I set Email
      And I set Password "1234"
      And I set First name as "XYz"
      And I set Last name as "gfd"
      And I select gender as "Male"
      And I set dob as "5/1/2022"
      And I set customer role as "Registered"

      @SB_01
  Scenario: Verify user able to add new customer
    Given I click on add new button
      And I set Email
      And I set Password "1234"
      And I set First name as "XYz"
      And I set Last name as "gfd"
      And I select gender as "Male"
      And I set dob as "5/1/2022"
      And I set customer role as "Admin"

@SB_01
  Scenario: Verify user able to add new customer
    Given I click on add new button
      And I set Email
      And I set Password "1234"
      And I set First name as "XYz"
      And I set Last name as "gfd"
      And I select gender as "Male"
      And I set dob as "5/1/2022"
      And I set customer role as "Forum"
      And I wait 10 seconds
@SB_01
  Scenario: Verify user able to add new customer
    Given I click on add new button
      And I set Email
      And I set Password "1234"
      And I set First name as "XYz"
      And I set Last name as "gfd"
      And I select gender as "Male"
      And I set dob as "5/1/2022"
      And I set customer role as "Guest"
      And I wait 10 seconds
@SB_01
  Scenario: Verify user able to add new customer
    Given I click on add new button
      And I set Email
      And I set Password "1234"
      And I set First name as "XYz"
      And I set Last name as "gfd"
      And I select gender as "Male"
      And I set dob as "5/1/2022"
      And I set customer role as "Vender"
      And I wait 10 seconds

  @Varsha
  Scenario: Verify user able to add new customer
    Given I click on add new button
      And I set Email
      And I set Password "1234"
      And I set First name as "XYz"
      And I set Last name as "gfd"
      And I select gender as "Male"
      And I set dob as "5/1/2022"
      And I set customer role as "Registered"
      And I set customer role as "Admin"
      And I set customer role as "Forum"
      And I set customer role as "Guest"
      And I set customer role as "Vender"

