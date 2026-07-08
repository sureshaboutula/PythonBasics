Feature: Order Transaction
  Test Related to order transactions

  Scenario Outline: Verify order success message shown in details page
    Given place the item order with <username> and <password>
    And the user is on landing page
    When I login to portal with <username> and <password>
    And Navigate to orders page
    And Select the orderId
    Then order message is successfully displayed
    Examples:
      | username            | password  |
      | sureshabo@gmail.com | Deva@2024 |

