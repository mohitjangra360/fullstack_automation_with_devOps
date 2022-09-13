# Created by rupali at 07/09/2022
Feature: Common Statistics
  1. Verify user is able to see Common statistics under dashboard
  2. Verify user is able to click on expand icon of Common statistics
  3. Verify user is able to see items in common statistics
  4. Verify user is able to click on collapse icon of Common statistics
  5. Verify user is able to click on More info of items in common statistics
  Background:
  Given Open Browser
  And User On Login Page
  And User login as admin

  @D_CS_01
  Scenario: Verify user is able to see Common statistics under dashboard
    Given user is able to see "Common statistics" under dashboard
    And Close Browser

  @D_CS_02
  Scenario: Verify user is able to click on expand icon of Common statistics
    Given user is able to see "Common statistics" under dashboard
    Then Verify user must be able to see Expand button for "Common statistics" is visible
    And Click on expand icon of "Common statistics"
    And Close Browser

  @D_CS_03
  Scenario: Verify user is able to see items in common statistics
      Given user is able to see "Common statistics" under dashboard
      Then Verify user must be able to see Expand button for "Common statistics" is visible
      And Click on expand icon of "Common statistics"
      Then Verify user is able to see items in common statistics
      And Close Browser

  @D_CS_04
  Scenario: Verify user is able to click on collapse icon of Common statistics
      Given user is able to see "Common statistics" under dashboard
      Then Verify user must be able to see Expand button for "Common statistics" is visible
      And Click on expand icon of "Common statistics"
      Then Verify user is able to see items in common statistics
      And Click on collapse icon of "Common statistics"
      And Close Browser
