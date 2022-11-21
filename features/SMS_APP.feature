# Created by Aditya at 12-10-2022
Feature: Demo of SMS APP

  Background:
    Given Open Browser and salesforce
    And I am On Salesforce Login Page
    And I Login

    Scenario: Verify outgoings from standard objects on classic
      Given Verify user must be on classic page.
      And Verify user must be on "360 SMS" App layout.
      Then Click on "Contacts" object
      Then Verify "All Contacts" selected and Click GO
      And Click record from list
      Then Click send sms button on record page
      And Verify Send SMS page details
      Then Write Text in textbox field and click send
      Then Click on "SMS History" object and Click Go and verify "All" selected
