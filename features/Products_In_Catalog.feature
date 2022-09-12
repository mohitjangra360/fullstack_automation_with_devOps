# Created by Mohit at 12-09-2022
  @Products @Catalog
Feature: Product In Catalog
  # Enter feature description here
  Background:
    Given Open Browser
    And I am on Login Page
    And I login as admin

  Scenario: Verify Content Header On Products Page
    Given I should see "Add new"
#    Given I should see button "<string>" with <string>