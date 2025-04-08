Feature: Reelly Secondary listings page tests


#  Scenario: User can page through secondary pages
#    Given Open Reelly login page
#    When Input email address
#    And Input password
#    And Click on login button
#    And Click on Secondary
#    Then Verify that the Secondary page opens
#    When Click through all 132 pages

  Scenario: User can filter the Secondary deals by Unit price range
    Given Open Reelly login page
    When Input email address
    And Input password
    And Click on login button
    And Click on Secondary
    Then Verify that the Secondary page opens
    When Click on Filter button
    And Input 1200000 into From price field
    And Input 2000000 into To price field
    And Click Apply Filter button
    Then Click through all 26 pages and verify price in all cards inside the range 1200000 to 2000000
