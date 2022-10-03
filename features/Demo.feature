# Created by Aditya at 29-09-2022
Feature: Demo Pdf Content Access
  # Enter feature description here

  Background:
    Given Open Demo Browser
    And I click on Log In
    And I am On Demo Login Page
    And I login as Demo admin

  Scenario: Add product to cart
    Given I verify product visible on home page and click "Add to cart"
    Then I click on "Add to cart" and verify product in cart
    And I click on "Checkout" and confirm order
    Then Go to "Orders" and verify ordered product detail
    Then Click download invoice and verify product details

