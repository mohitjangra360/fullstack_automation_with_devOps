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
    And I am On Login Page
    And I login as admin
    Then I Select "Products" from "Catalog"
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

  @PL_08
  Scenario: Verify user able to create new products
    Given I click on add new button
    And I wait 2 seconds
    And I set product name "Product name"
    And I set short description "fgdsg"
    And I set full description "fdsfds sadasdasdas TEST"
    And I select categories first "Computers" and second "Computers >> Notebooks"
    And I select manufacturers "Apple"
    And I set Product tags "Computer"
    And I set Product type "Simple"
    And I set customer role as "Guests"
    And I set Vendor type "Vendor 1"
    And I set Available start date "9/23/2022 12:00 AM"
    And I set Available end date "11/22/2022 12:00 AM"
    And I set price "500"
    Then Click "save"
    Then I should see saved successfully message


  @PL_12
  Scenario: Verify user must be able to import products using import button
    Given user should see "Import" button
    And user should click on "Import" button
    And I wait 4 seconds
    And user should see popup message "Import from Excel"
    And user should select path "C:\nopcommnerce\Test_Data\products.xlsx"
    And user should click to "Import from Excel" button
    And I wait 2 seconds
    Then user should see the Error Message of "Products" after click on import from excel


  @PL_13
  Scenario: Verify user must be able to see and click on "Delete(Selected)" button
    Given I should able to see "Delete (selected)" Button
    Then I should able to select product to delete
    And I wait 10 seconds
    And I should able to click "Delete (selected)" Button
    Then I should able to click YES on Delete POPUP
    And I wait 10 seconds

    @PL_15
  Scenario: Verify  user must be able to search products by warehouse
    Given I should see "SearchWarehouseId" select field by id
    And I should click "SearchWarehouseId" select field by "id" and select "Warehouse 1 (New York)"
    Then I should click "Search"
    And I see search result by Warehouse and count number of items


  @PL_19
  Scenario: Verify  user must be able to search products by products type
    Given user should select products types "Simple"
    And I wait 2 seconds
    And I should click on "Search" button on product page
    And I wait 4 seconds

  @PL_20
  Scenario: Verify  user must be able to search products by SKU
    Given I should see Go directly to product SKU field
    Then I should able to enter product SKU DS_VA3_PC
    Then I should able to click on Go button
    And I wait 5 seconds
    Then I should see SKU DS_VA3_PC on edit page of that product

  @PL_22
  Scenario: Verify user must be select multiple product in table by checkbox
    Given I should see data table
    And I should click all items checkboxes


  @PL_27
  Scenario: Verify user must be able to change product SKU number under product info
    Given I should see see product table
    Then I should see edit button of product Apple MacBook Pro 13-inch & able to click on that
    Then I should see the product SKU field
    Then I should able to change product Sku field by AP_MBP_15 with tag input & save it


  @PL_29
  Scenario: Verify user must be able to change product manufacturer under product info
    Given I should see data table
    And I should edit "Build your own computer" details by click "Edit"
    Then I should see "Edit product details - Build your own computer"
    And I select manufacturers "Apple"
    Then Click "save"
    Then I should see saved successfully message


  @PL_33
  Scenario: Verify user must be able to change product checkbox as show on home page under product info
     Given user should be able to see Edit button
     And user should able to click on Edit button
     And I wait 3 seconds
     And user should checked on checkbox
     And I wait 6 seconds
     And I set display order value "3"

  @PL_34
  Scenario: Verify user must be able to change Product type under product info
    Given I should see see product table
    Then I should see edit button of product Apple MacBook Pro 13-inch & able to click on that
    Then I should see the product Product type field
    Then I should able to change product ProductType field by Grouped (product with variants) with tag select & save it


  @PL_36
  Scenario: Verify user must be able to change product customer role under product info
    Given I should see data table
    And I should edit "Apple MacBook Pro 13-inch" details by click "Edit"
    Then I should see "Edit product details - Apple MacBook Pro 13-inch"
    And I set customer role as "Guests"
    Then Click "save"
    Then I should see saved successfully message


  @PL_40
  Scenario: Verify user must be able to change product available start date under product info
    Given user should be able to see "Edit" button
    And user should able to click on "Edit" button
    And I wait 2 seconds
    And user should set "12/2/2022 12:00 AM" on product available start date field
    And I wait 3 seconds
    And user should be able to click on "Save" button
    And I wait 10 seconds

  @PL_41
  Scenario: Verify user must be able to change product available end date under product info
    Given I should see see product table
    Then I should see edit button of product Apple MacBook Pro 13-inch & able to click on that
    Then I should see the product Available end date field
    Then I should able to change product AvailableEndDate field by 10/10/2022 1:00:00 PM with tag input & save it


  @PL_43
  Scenario: Verify user must be able to change product Mark as new and Start date under product info
    Given I should see data table
    And I should edit "HP Spectre XT Pro UltraBook" details by click "Edit"
    Then I should see "Edit product details - HP Spectre XT Pro UltraBook"
    And I should Enable checkbox of "MarkAsNew"
    And I set Available start date "9/23/2022 12:00 AM"
    And I set Available end date "11/22/2022 12:00 AM"
    Then Click "save"
    Then I should see saved successfully message

  @PL_48
  Scenario: Verify user must be able to change product cost under product prices
    Given I should see see product table
    Then I should see edit button of product Apple MacBook Pro 13-inch & able to click on that
    Then I should see the product Product cost field
    Then I should able to change product cost field by 120 & save it


  @PL_50
  Scenario: Verify user must be able to change product shipping weight under shipping
    Given I should see data table
    And I should edit "Apple MacBook Pro 13-inch" details by click "Edit"
    Then I should see "Edit product details - Apple MacBook Pro 13-inch"
    And I set shipping weight "500"
    Then Click "save"
    Then I should see saved successfully message

  @PL_55
   Scenario: Verify user must be able to change product delivery date under shipping
    Given I should see see product table
    Then I should see edit button of product Apple MacBook Pro 13-inch & able to click on that
    Then I should see the product Delivery date field
    Then I should able to change product DeliveryDate field by 1-2 days with tag select & save it


  @PL_57
  Scenario: Verify user must be able to change product Stock quantity under inventory
    Given I should see data table
    And I should edit "Apple MacBook Pro 13-inch" details by click "Edit"
    Then I should see "Edit product details - Apple MacBook Pro 13-inch"
    And I set Minimum qty "1000"
    And I set Maximum qty "1000"
    Then Click "save"
    Then I should see saved successfully message

  @PL_62
    Scenario: Verify user must be able to change product backorders under inventory
     Given I should see see product table
     Then I should see edit button of product Apple MacBook Pro 13-inch & able to click on that
     Then I should see the product Backorders field
     Then I should able to change product Backorder field by Allow qty below 0 with tag select & save it


  @PL_64
  Scenario: Verify user must be able to change product  maximum cart qty under inventory
    Given I should see data table
    And I should edit "Apple MacBook Pro 13-inch" details by click "Edit"
    Then I should see "Edit product details - Apple MacBook Pro 13-inch"
    And I set Maximum qty "1000"
    Then Click "save"
    Then I should see saved successfully message
