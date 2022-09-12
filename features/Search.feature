# Created by Aditya at 11-09-2022
Feature: Search (1. Verify user able to click or input into search bar)
  1. Verify user must be able to see Search bar on Dashboard
  2. Verify user must be able to click in Search bar
  3. User input "al","all","Plugin","plug",etc.
  4. Verify user must be able to see the related data in dop down according to there search keyword

  Background:
  Given Open Browser
  And User On Login Page
  And User login as admin

  @SR_01
  Scenario: Verify user must be able to see Search bar on Dashboard
    Given User should see Searchbar
    And User able to click in Search bar

