Feature: Reelly Settings page tests


#  Scenario: User can change their password
#    Given Open Reelly login page
#    When Input email address
#    And Input password
#    And Click on login button
##    And Click on Main Menu # used for mobile testing
##    And Click on user profile image # used for mobile testing
#    And Click on settings
#    And Click on Change Password option
#    Then Verify Change Password page opens
#    When Input test password into input fields
#    Then Verify Change Password button is available to click

  Scenario: User sees 12 options on settings page
    Given Open Reelly login page
    When Input email address
    And Input password
    And Click on login button
    And Click on Settings
    Then Verify there are 12 settings options
    Then Verify Connect the Company button is available

