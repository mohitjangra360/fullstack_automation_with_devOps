# Created by Ekta at 14-09-2022
Feature: Product page
  1.User should be able to see export button
2.Click on export button with following column
>Export to XML(all found)
>Export to XML(selected)
>Export to Excel(all found)
>Export to Excel(selected)
3.Click on Export Button for download.

  Background:
  Given Open Browser
  And User On Login Page
  And User login as admin
    And Select "Products" from "Catalog"


  Scenario: User able to see export button
   Given User should see export
    And User able to click in export

