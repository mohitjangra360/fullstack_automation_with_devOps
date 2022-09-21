# Created by Aditya at 20-09-2022
Feature: Manufacturer Delete (selected)
  # Enter feature description here

  Background:
    Given Open Browser
    And User On Login Page
    And User login as admin

  @DL_01
  Scenario: IMPORT ACTIONS
    Given Verify user must be able to go on "Manufacturers" from "Catalog"
    Given Verify user must be able to see "Delete (selected)" Button
    And Verify user must be able to click "Delete (selected)" Button
    And Verify user must be able to click YES on Delete POPUP