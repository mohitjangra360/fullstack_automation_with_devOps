# Created by rupali at 12/09/2022
Feature: Product List and Product Edit
  1. Verify Product list columns
  2. Verify user is able to change the value of show items and verify the value
  3. Verify User is able to edit the product from product list

  Background:
    Given Open Browser
    And User On Login Page
    And User login as admin
    Then Select "Products" from "Catalog"

  @C_PL_01
  Scenario: Verify Product list columns
    Given I should see columns in Product list

  @C_PL_02
  Scenario: Verify user is able to change the value of show items and verify the value
    Given I should able to change value "7" of show items
    Then I wait 5 seconds
    And I should able to verify value of show items selected "7" and items display
    Then I wait 5 seconds

    @C_PL_03
    Scenario: Verify User is able to edit the product from product list
      Given I should able to click on edit btn of first product in list

    @C_PL_04
    Scenario: Verify User is able to edit the product from product list
      Given I should able to click on edit btn of first product in list
      Then I verify cards under advance mode
      Then I edit the fields under card "Product info"
      Then I edit Product name with "Product-edit"
      Then I edit Short description with "this is my description"
      And I wait 5 seconds
      Then I edit Full description with "this is my full description"
      And I wait 5 seconds
      Then I edit SKU with "Test SKU"
      Then I click on Published checkbox
      And I wait 10 seconds
#      And click on back to Product list

    @C_PL_05
    Scenario: Verify User is able to edit the product from product list
      Given I should able to click on edit btn of first product in list
      Then I switch from advance to basic mode
      Then I verify cards under basic mode
      Then I edit the fields under each card
      And click on back to Product list