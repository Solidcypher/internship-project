Feature: Reelly password management tests


  Scenario: User can change their password
    Given Open Reelly login page
    When Input email address
    And Input password
    And Click on login button
    And Click on Main Menu
    And Click on user profile image
    # And Click on settings
    And Click on Change Password option
    Then Verify Change Password page opens
    When Input test password into input fields
    Then Verify Change Password button is available to click
