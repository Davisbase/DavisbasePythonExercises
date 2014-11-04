Feature: Pricing

    Exercise: Implement this simple feature, backed by a simple in-memory data structure.

    As a customer
    I want to be told the price of animals
    so that I can make purchasing decisions

Scenario: Dog Search
    Given a Dog costs 23
    When I enter Dog and search for price
    Then the result should be 23

Scenario: Cat Search
    Given a Cat costs 45
    When I enter Dog and search for price
    Then the result should be 45

Scenario Outline: Bulk Pet Searches
    Given a <pet name> costs <price>
    When I enter <pet name> and search for price
    Then the result should be <price>

Examples:
    | pet name   | price |
    | Dog          | 23  |
    | Cat          | 13  |
