# Created by rupali at 07/09/2022
Feature: Common Statistics
  # Enter feature description here
Background:
  Given Open Browser
  And User On Login Page
  And User login as admin

@D_CS_01
  Scenario: Verify user is able to see Common statistics under dashboard
    Given user is able to see Common statistics under dashboard
