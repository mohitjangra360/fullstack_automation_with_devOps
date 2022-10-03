# Created by Mohit at 26-09-2022
Feature: Catalog >> Category
  # Enter feature description here
  Background:
    Given Open Browser
    And I am On Login Page
    And I login as admin
    Then I Select "Categories" from "Catalog"

  @CC_01 @Aditya
  Scenario:Verify user must be able to see and click on "Add new" button
    Given I should see "Add new" button
    And I click on add new button
    Then I should see "back to category list"


  @CC_02 @Rupali
  Scenario: Verify user must be able to see and click on "Export" button
    Given I should see "Export" button
    And I click On Export button
    Then I should see Export to XML
    Then I should see Export to Excel

  @CC_03 @Aditya
  Scenario: Verify user must be able to see and click on "Import" button
    Given Verify user must be able to see "Import" Button
    And Verify user must be able to click on "Import" Button
    And Verify user must be able to see "Import from Excel" choose file POP UP window
    And Verify user must be able to select Import file path "D:\data\\products (1).xlsx"
    And Verify user must be able to click button of "Import from Excel"
    And Verify user must be able to see the Error Message of "Categories" POP UP

    @CC_04 @Rupali
  Scenario: Verify user must be able to see and click on "Delete(Selected)" button
    Given I should see Delete(Selected) button
    And I click on delete(selected) button
    And I wait 3 seconds
    Then I should see "Are you sure?"

  @CC_05 @Aditya
  Scenario: Verify user must be able to add new category
    Given I click on add new button
    And I wait 2 seconds
    And I set product name "Category name"
    And I set description "fdsfds sadasdasdas TEST"
    And I select parent category "Electronics"
    Then Click "save"
    Then I should see saved successfully message


  @CC_06 @Rupali
  Scenario: Verify user must be able to download category list as "Export To XML"
    Given I should see "Export" button
    And I click On Export button
    Then I should see Export to XML
    Then I should able to click on Export to XML Export to XML
    And I wait 10 seconds
    Then I should see downloaded file

  @CC_07 @Aditya
  Scenario: Verify user must be able to see export option under export button
    Given Verify user must be able to see "Export" Button
    And Verify user must be able to click on drop down options button and select "Export to Excel"
    And Verify user must be able to check downloaded Export file from "C:\Users\User\Downloads\categories.xlsx"

    @CC_08 @Rupali
  Scenario: Verify user must be able to import category
    Given I should see Import button
    Then I click on import button
    Then I should see choose file popup box
    Then I should able to select import file path "C:\Users\rupal\Downloads\categories.xlsx"
    Then I should able to click button of "Import from Excel"
    And I should see message of "Categories" POP UP


  @CC_09 @Aditya
  Scenario: Verify user must be able to delete selected category
    Given Verify user must be able to select "Apparel" checkbox to Delete
    Given Verify user must be able to see "Delete (selected)" Button
    And Verify user must be able to click "Delete (selected)" Button by name
    And Verify user must be able to click YES on Delete POPUP

    @CC_10 @Rupali
  Scenario: Verify user must be able to search category with name via All
    Given I should see "SearchCategoryName" input field by id
    Then I should able to enter category name "Electronics" in search
    Then I should see Published field and select value "Published only"
    Then I should click "Search"
    Then I see search result by Published field and count number of items


  @CC_11 @Aditya
  Scenario: Verify user must be able to search category with name via Published only
    Given I should see search "SearchPublishedId" select field by "id"
    And I should click "SearchPublishedId" select field by "id" and select "Published only"
    Then I should click "Search"
    And I see search result by Published Only and Verify

    @CC_12 @Rupali
  Scenario: Verify user must be able to search category with name via Unpublished only
    Given I should see "SearchCategoryName" input field by id
    Then I should able to enter category name "Electronics" in search
    Then I should see Published field and select value "Unpublished only"
    Then I should click "Search"
    Then I see search result by Published field and count number of items

  @CC_13 @Aditya
  Scenario: Verify user must be able to edit any category from table
    Given I should see data table
    And I should edit "Gift Cards" details by click "Edit"
    Then I should see "Edit category details - Gift Cards"
    And I select parent category "Electronics"
    Then Click "save"
    Then I should see saved successfully message


  @CC_14 @Rupali
  Scenario: Verify user must be able to change category name under category info
    Given I should see see category table
    Then I should edit "Jewelry" details by click "Edit" under category
    And I wait 5 seconds
    Then I should see "Name" input field by id
    Then I should able to enter category name as test 123
    Then I should able to click save Save Button
    And I wait 10 seconds
    Then I should see saved successfully message on category

  @CC_15 @Aditya
  Scenario: Verify user must be able to change category description under category info
    Given I should see data table
    And I should edit "Gift Cards" details by click "Edit"
    Then I should see "Edit category details - Gift Cards"
    And I set description "fdsfds sadasdasdas TEST"
    Then Click "save"
    Then I should see saved successfully message

    @CC_16 @Rupali
  Scenario: Verify user must be able to change category parent category under category info
    Given I should see see category table
    Then I should edit "Jewelry" details by click "Edit" under category
    And I wait 5 seconds
    Then I should see "ParentCategoryId" select field by id
    Then I should able to select Parent category as Apparel >> Shoes
    Then I should able to click save Save Button
    Then I should see saved successfully message on category

  @CC_17 @Aditya
  Scenario: Verify user must be able to change category picture under category info
    Given I should see data table
    And I should edit "Gift Cards" details by click "Edit"
    Then I should see "Edit category details - Gift Cards"
    And Verify user must be able to select picture file "D:\data\Sample Image 1.png"
    Then Click "save"
    Then I should see saved successfully message

    @CC_18 @Rupali
  Scenario: Verify user must be able to change category published status checkbox as true or false under display
    Given I should see see category table
    Then I should edit "Jewelry" details by click "Edit" under category
    And I wait 5 seconds
    Then I should able to see and click on checkbox of Published by id Published
    Then I should able to click save Save Button
    Then I should see saved successfully message on category

  @CC_19 @Aditya
  Scenario: Verify user must be able to change category show on home page checkbox as true or false under display
    Given I should see data table
    And I should edit "Gift Cards" details by click "Edit"
    Then I should see "Edit category details - Gift Cards"
    And Click checkbox of "show on home page"
    Then Click "save"
    Then I should see saved successfully message

    @CC_20 @Rupali
  Scenario: Verify user must be able to change category include top in menu checkbox as true or false under display
    Given I should see see category table
    Then I should edit "Jewelry" details by click "Edit" under category
    And I wait 5 seconds
    Then I should able to see and click on checkbox of Include in top menu by id IncludeInTopMenu
    Then I should able to click save Save Button
    Then I should see saved successfully message on category

  @CC_21 @Aditya
  Scenario: Verify user must be able to change category allow customer to select page size checkbox as true or false under display
    Given I should see data table
    And I should edit "Gift Cards" details by click "Edit"
    Then I should see "Edit category details - Gift Cards"
    And Click checkbox of "Allow customers to select page size"
    Then Click "save"
    Then I should see saved successfully message


  @CC_22 @Rupali
  Scenario: Verify user must be able to change category price range filter checkbox as true or false under display
    Given I should see see category table
    Then I should edit "Jewelry" details by click "Edit" under category
    And I wait 5 seconds
    Then I should able to see and click on checkbox of Price range filtering by id PriceRangeFiltering
    Then I should able to click save Save Button
    Then I should see saved successfully message on category

  @CC_23 @Aditya
  Scenario: Verify user must be able to change category display order under display
    Given I should see data table
    And I should edit "Gift Cards" details by click "Edit"
    Then I should see "Edit category details - Gift Cards"
    And I set display order "34567"
    Then Click "save"
    Then I should see saved successfully message








