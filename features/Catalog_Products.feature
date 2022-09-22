# Created by Mohit at 21-09-2022
Feature: Catalog >> Products
  1. Verify user must be able to see and click on "Add new" button
  2. Verify user must be able to see and click on "Download catalog as pdf" button
  3. Verify user must be able to see and click on "Export" button
  4. Verify user must be able to see and click on "Import" button
  5. Verify user must be able to see and click on "Delete(Selected)" button
  6. Verify user must be able to see export option under export button
  7. Verify user must be able to click on export option under export button
  8. Verify user able to create new products
  Verify user must be able to switch basic to advance and advanced to basic setting under add new products
  Verify user must be able to download catalog as pdf
  Verify user must beb able to download all products using export to method
  Verify user must be able to import products using import button
  Verify user must be able to delete selected products
  Verify  user must be able to search products by name
  Verify  user must be able to search products by warehouse
  Verify  user must be able to search products by category
  Verify  user must be able to search products by Manufacturer
  Verify  user must be able to search products by Vendor
  Verify  user must be able to search products by products type
  Verify  user must be able to search products by SKU
  Verify user must be able to see products table
  Verify user must be select multiple product in table by checkbox
  Verify user must be able to edit products
  Verify user must be able to change product name under product info
  Verify user must be able to change product short description under product info
  Verify user must be able to change product full description under product info
  Verify user must be able to change product SKU number under product info
  Verify user must be able to change product category under product info
  Verify user must be able to change product manufacturer under product info
  Verify user must be able to change product tag under product info
  Verify user must be able to change product GTIN under product info
  Verify user must be able to change product manufacturer part number under product info
  Verify user must be able to change product checkbox as show on home page under product info
  Verify user must be able to change product type under product info
  Verify user must be able to change product template under product info
  Verify user must be able to change product customer role under product info
  Verify user must be able to change product limited to store under product info
  Verify user must be able to change product vendor under product info
  Verify user must be able to change product allow for review under product info
  Verify user must be able to change product available start date under product info
  Verify user must be able to change product  available end date under product info
  Verify user must be able to change product mark as new under product info
  Verify user must be able to change product Mark as new. Start date under product info
  Verify user must be able to change product Mark as new. End date under product info
  Verify user must be able to change product Admin comment under product info
  Verify user must be able to change product price under product prices
  Verify user must be able to change product old price  under product prices
  Verify user must be able to change product cost under product prices
  Verify user must be able to change product shipping enable checkbox under shipping
  Verify user must be able to change product shipping weight under shipping
  Verify user must be able to change product shipping length under shipping
  Verify user must be able to change product shipping width under shipping
  Verify user must be able to change product shipping height under shipping
  Verify user must be able to change product  free shipping checkbox under shipping
  Verify user must be able to change product delivery date under shipping
  Verify user must be able to change product inventory method under inventory
  Verify user must be able to change product Stock quantity under inventory
  Verify user must be able to change product warehouse under inventory
  Verify user must be able to change product minimum stock qty under inventory
  Verify user must be able to change product low stock activity under inventory
  Verify user must be able to change product Notify for qty below under inventory
  Verify user must be able to change product backorders under inventory
  Verify user must be able to change product minimum cart qty under inventory
  Verify user must be able to change product  maximum cart qty under inventory
  Verify user must be able to change product allowed qty under inventory
  Verify user must be able to upload product picture under picture
  Verify user must be able to edit product picture under picture
  Verify user must be able to delete product picture under picture
  Background:
    Given Open Browser
    And I am on Login Page
    And I login as admin
    Then Select " Products" from "Catalog"
#    Then I am goto "Products" Page


  @PL_01
  Scenario: Verify user must be able to see and click on "Add new" button
    Given I should see "Add new" button
    And I click on add new button
    Then I should see "back to product list"
    
  @PL_02
  Scenario: Verify user must be able to see and click on "Download catalog as pdf" button
    Given I should see "Download catalog as pdf" button
    Then I click on "Download catalog as pdf" button

  @PL_03
  Scenario: Verify user must be able to see and click on "Export" button
    Given I should see "Export" button
    And I click On Export button
    Then I should see Export to XML (all found)

  @PL_04
  Scenario: Verify user must be able to see and click on "Import" button
    Given I should see Import button
    And I click on import button
    Then I should see choose file popup box

  @PL_05
  Scenario: Verify user must be able to see and click on "Delete(Selected)" button
    Given I should see Delete(Selected) button
    And I click on delete(selected) button
    And I wait 3 seconds
    Then I should see "Are you sure?"

  @PL_06
  Scenario: Verify user must be able to see export option under export button
    Given I should see "Export" button
    And I click On Export button
    Then I should see Export to XML (all found)
    Then I should see Export to XML (selected)
    Then I should see Export to Excel (all found)
    Then I should see Export to Excel (selected)

#  @PL_07
#  Scenario: Verify user must be able to click on export option under export button
#    Given I should see "Export" button
#    And I click On Export button
#    hold par hai

  @PL_08
  Scenario: Verify user able to create new products
    Given I click on add new button
    And I wait 5 seconds
    And I set product name "Mohit"
    And I set short description "fgdsg"
    And I set full description "fdsfds"
    And I set Email
    And I set Password "1234"
    And I set First name as "XYz"
    And I set Last name as "gfd"
    And I select gender as "Male"
    And I set dob as "5/1/2022"
    And I set customer role as "Registered"

    
