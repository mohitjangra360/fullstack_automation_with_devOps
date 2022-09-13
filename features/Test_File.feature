# Created by Mohit at 12-09-2022
Feature: SideBar
  # Enter feature description here
  Background:
    Given Open Browser
    And User On Login Page
    And User login as admin

    @SB_01
  Scenario: Verify Side Bar Logo Is Visible
    Given I should see logo

    @SB_02
  Scenario: Verify Side Bar Search Box Is Visible
    Given I should see search box

     @SB_03
  Scenario: Verify side menu bar item is visible as main header
       Given I should see all side menu item is visible

  Scenario: Verify user able to select and click on side menu item
#    Given Select "Customer reports" from "Reports"
    Given I goto Report >> Customer reports >> Customer by order total
