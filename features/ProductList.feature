# Created by rupali at 12/09/2022
Feature: Product List and Product Edit
  1. Verify Product list columns

  Background:
    Given Open Browser
    And User On Login Page
    And User login as admin
    Then I Select "Products" from "Catalog"

  @C_PL_01
  Scenario: Verify Product list columns
    Given I should see columns in Product list

