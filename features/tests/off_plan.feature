Feature: Reelly Off-Plan page tests


  #Scenario 17
  Scenario: User can open the off plan page and go through the pagination
    Given Open Reelly login page
    When Input email address
    And Input password
    And Click on login button
    And Click on Off-Plan old
    Then Verify old Off-Plan page opens
    When Click through all Off Plan pages
    And Return to first page using last page button