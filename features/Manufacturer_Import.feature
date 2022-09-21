# Created by Aditya at 20-09-2022
Feature: MANUFACTURER IMPORT
  # Enter feature description here

  Background:
    Given Open Browser
    And User On Login Page
    And User login as admin

  @CA_IM_01
  Scenario: PRODUCT IMPORT ACTIONS
    Given Verify user must be able to go on "Manufacturers" from "Catalog" product page
    Given Verify user must be able to see "Import" Button on Product Page
    And Verify user must be able to click on "Import" Button
    And Verify user must be able to see "Import from Excel" choose file POP UP window
    And Verify user must be able to select Import file path "D:\data\\categories.xlsx"
    And Verify user must be able to click button of "Import from Excel"
    And Verify user must be able to see the Error Message of "Manufacturers" POP UP