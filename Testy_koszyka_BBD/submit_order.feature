Feature: An already registered user wants to place an order
  Background:
    Given User is on main page
    And User is logged in

  Scenario: TP-389 The user wants to place an order with one product
    When The user adds one product to the cart
    And The user goes to the cart and clicks Proceed to checkout
    And The user passes login verification and click Proceed to checkout
    And The user confirms his address and clicks Proceed to checkout
    And The user is entering the payment details correctly and klick Confirm
    Then Order placed
    And The user goes to the home page

  Scenario: TP-390 The user wants to place an order with 17e+307 products
    When The user adds 17e+307 products to the cart
    And The user goes to the cart and clicks Proceed to checkout
    And The user passes login verification and click Proceed to checkout
    And The user confirms his address and clicks Proceed to checkout
    And The user is entering the payment details correctly and klick Confirm
    Then Order placed
    And The user goes to the home page

  Scenario: TP-391 The user wants to place an order with two products
    When The user adds two different products to the cart
    And The user goes to the cart and clicks Proceed to checkout
    And The user passes login verification and click Proceed to checkout
    And The user confirms his address and clicks Proceed to checkout
    And The user is entering the payment details correctly and klick Confirm
    Then Order placed
    And The user goes to the home page

  Scenario: TP-392 The user wants to place an order with a non-integer number of products
    When The user adds a non-integer number products to the cart
    And The user goes to the cart and clicks Proceed to checkout
    And The user passes login verification and click Proceed to checkout
    And The user confirms his address and clicks Proceed to checkout
    And The user is entering the payment details correctly and klick Confirm
    Then Order placed
    And The user goes to the home page

  Scenario: TP-393 An unregistered user wants to place an order
    When The user logs out
    And The user adds a one product to the cart
    And The user goes to the cart and clicks Proceed to checkout
    And The user logs in
    And The user confirms his address and clicks Proceed to checkout
    And The user is entering the payment details correctly and klick Confirm
    Then Order placed
    And The user goes to the home page

  Scenario: TP-394 An unregistered user wants to place an order without logging
      When The user logs out
      And The user adds a one product to the cart
      And The user goes to the cart and clicks Proceed to checkout
      And The user tries to log in without entering any data
      Then Order is not placed
      And The user goes to the home page

  Scenario: TP-395 Placing an order with deleting the address
    When The user adds one product to the cart
    And The user goes to the cart and clicks Proceed to checkout
    And The user passes login verification and click Proceed to checkout
    And The user deletes his address
    Then Order did not place, the address is required
    And The user goes to the home page

  Scenario: TP-396 Placing an order with deleting city
    When The user adds one product to the cart
    And The user goes to the cart and clicks Proceed to checkout
    And The user passes login verification and click Proceed to checkout
    And The user deletes his city
    Then Order did not place, city is required
    And The user goes to the home page

  Scenario: TP-397 Placing an order with deleting state
    When The user adds one product to the cart
    And The user goes to the cart and clicks Proceed to checkout
    And The user passes login verification and click Proceed to checkout
    And The user deletes his state
    Then Order did not place, state is required
    And The user goes to the home page

  Scenario: TP-398 Placing an order with deleting country
    When The user adds one product to the cart
    And The user goes to the cart and clicks Proceed to checkout
    And The user passes login verification and click Proceed to checkout
    And The user deletes his country
    Then Order did not place, country is required
    And The user goes to the home page

  Scenario: TP-396 Placing an order with deleting the postalcode
    When The user adds one product to the cart
    And The user goes to the cart and clicks Proceed to checkout
    And The user passes login verification and click Proceed to checkout
    And The user deletes his postalcode
    Then Order did not place, the postalcode is required
    And The user goes to the home page

  Scenario: TP-400 Placing an order without entering the account name
    When The user adds one product to the cart
    And The user goes to the cart and clicks Proceed to checkout
    And The user passes login verification and click Proceed to checkout
    And The user confirms his address and clicks Proceed to checkout
    And The user is entering the payment details without account name and klick Confirm
    Then Order did not place, account name is required.
    And The user goes to the home page

  Scenario: TP-401 Placing an order without entering the account name
    When The user adds one product to the cart
    And The user goes to the cart and clicks Proceed to checkout
    And The user passes login verification and click Proceed to checkout
    And The user confirms his address and clicks Proceed to checkout
    And The user is entering the payment details without account name and klick Confirm
    Then Order did not place, account name is required.
    And The user goes to the home page

  Scenario: TP-402 Placing an order without entering the payment-method
    When The user adds one product to the cart
    And The user goes to the cart and clicks Proceed to checkout
    And The user passes login verification and click Proceed to checkout
    And The user confirms his address and clicks Proceed to checkout
    And The user is entering the payment details without account number and klick Confirm
    Then Order did not place, account number is required.
    And The user goes to the home page

  Scenario: TP-403 Placing an order without entering payment details
    When The user adds one product to the cart
    And The user goes to the cart and clicks Proceed to checkout
    And The user passes login verification and click Proceed to checkout
    And The user confirms his address and clicks Proceed to checkout
    And The user does not enter payment details and klick Confirm'
    Then Order did not place, payment details are required.
    And The user goes to the home page
    And The User closes the browser

