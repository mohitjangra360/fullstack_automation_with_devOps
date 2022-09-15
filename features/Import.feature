# Created by Aditya at 13-09-2022
Feature: IMPORT
  # Enter feature description here

  Background:
  Given Open Browser
  And User On Login Page
  And User login as admin

  @IM_01
  Scenario: IMPORT ACTIONS
    Given Verify user must be able to go on "Products" from "Catalog" product page
    Given Verify user must be able to see "Import" Button on Product Page
    And Verify user must be able to click on "Import" Button


