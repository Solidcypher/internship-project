Feature: Reelly Secondary listings page tests


  Scenario: User can page through secondary pages
    Given Open Reelly login page
    When Input email address
    And Input password
    And Click on login button
    And Click on Secondary
    Then Verify that the Secondary page opens
    When Click through all 99 pages