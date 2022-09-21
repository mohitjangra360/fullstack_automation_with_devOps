# Created by Mohit at 21-09-2022
Feature: Search Manufacture
  # Enter feature description here
  Background:
   Given Open Browser
    And User On Login Page
    And User login as admin
    Then select "Manufacturers" from "Catalog"


  Scenario: Verify user able to search manufacture by name
    Given I should see button "search-manufacturers" with id
    And I set search value as name "Apple"
    And I click on Search Button
    And I see search result by name "Nike"
    And I see search result by name "Apple"

    And I wait 10 seconds