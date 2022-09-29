# Created by Mohit at 26-09-2022
Feature: Catalog >> Category
  # Enter feature description here
  Background:
    Given Open Browser
    And I am On Login Page
    And I login as admin
    Then I Select "Categories" from "Catalog"

  @CC_01
  Scenario:Verify user must be able to see and click on "Add new" button
    Given I should see "Add new" button
    And I click on add new button
    Then I should see "back to category list"

  @CC_03
  Scenario: Verify user must be able to see and click on "Import" button
    Given Verify user must be able to see "Import" Button
    And Verify user must be able to click on "Import" Button
    And Verify user must be able to see "Import from Excel" choose file POP UP window
    And Verify user must be able to select Import file path "D:\data\\products (1).xlsx"
    And Verify user must be able to click button of "Import from Excel"
    And Verify user must be able to see the Error Message of "Categories" POP UP

  @CC_05
  Scenario: Verify user must be able to add new category
    Given I click on add new button
    And I wait 2 seconds
    And I set product name "Category name"
    And I set description "fdsfds sadasdasdas TEST"
    And I select parent category "Electronics"
    Then Click "save"
    Then I should see saved successfully message

  @CC_07
  Scenario: Verify user must be able to see export option under export button
    Given Verify user must be able to see "Export" Button
    And Verify user must be able to click on drop down options button and select "Export to Excel"
    And Verify user must be able to check downloaded Export file from "C:\Users\User\Downloads\categories.xlsx"

  @CC_09
  Scenario: Verify user must be able to delete selected category
    Given Verify user must be able to select "Apparel" checkbox to Delete
    Given Verify user must be able to see "Delete (selected)" Button
    And Verify user must be able to click "Delete (selected)" Button by name
    And Verify user must be able to click YES on Delete POPUP

  @CC_11
  Scenario: Verify user must be able to search category with name via Published only
    Given I should see search "SearchPublishedId" select field by "id"
    And I should click "SearchPublishedId" select field by "id" and select "Published only"
    Then I should click "Search"
    And I see search result by Published Only and Verify

  @CC_13
  Scenario: Verify user must be able to edit any category from table
    Given I should see data table
    And I should edit "Gift Cards" details by click "Edit"
    Then I should see "Edit category details - Gift Cards"
    And I select parent category "Electronics"
    Then Click "save"
    Then I should see saved successfully message

  @CC_15
  Scenario: Verify user must be able to change category description under category info
    Given I should see data table
    And I should edit "Gift Cards" details by click "Edit"
    Then I should see "Edit category details - Gift Cards"
    And I set description "fdsfds sadasdasdas TEST"
    Then Click "save"
    Then I should see saved successfully message

  @CC_17
  Scenario: Verify user must be able to change category picture under category info
    Given I should see data table
    And I should edit "Gift Cards" details by click "Edit"
    Then I should see "Edit category details - Gift Cards"
    And Verify user must be able to select picture file "D:\data\Sample Image 1.png"
    Then Click "save"
    Then I should see saved successfully message

  @CC_19
  Scenario: Verify user must be able to change category show on home page checkbox as true or false under display
    Given I should see data table
    And I should edit "Gift Cards" details by click "Edit"
    Then I should see "Edit category details - Gift Cards"
    And Click checkbox of "show on home page"
    Then Click "save"
    Then I should see saved successfully message

  @CC_21
  Scenario: Verify user must be able to change category allow customer to select page size checkbox as true or false under display
    Given I should see data table
    And I should edit "Gift Cards" details by click "Edit"
    Then I should see "Edit category details - Gift Cards"
    And Click checkbox of "Allow customers to select page size"
    Then Click "save"
    Then I should see saved successfully message

  @CC_23
  Scenario: Verify user must be able to change category display order under display
    Given I should see data table
    And I should edit "Gift Cards" details by click "Edit"
    Then I should see "Edit category details - Gift Cards"
    And I set display order "34567"
    Then Click "save"
    Then I should see saved successfully message








