# Created by rahul at 15-09-2022
Feature: Manufactures

  Background:
        Given Open Browser
        And User On Login Page
        And User login as admin
        Then select "Manufacturers" from "Catalog"


  Scenario: Verify user is able to see export button
    Given I should see export button
    And I click on export button
    And I should click on both dropdown list


