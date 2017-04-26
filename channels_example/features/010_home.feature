Feature: Test home page

    Scenario: See "Hello World"
        When I visit site page "/"
        Then I should see "Hello World"
        And I should see "The are no registered users."


    Scenario: See list of users
        Given I have users in the database:
            | username   |
            | test_user1 |
            | test_user2 |
        When I visit site page "/"
        Then I should see "List of users:"
        And I should see "test_user1"
        And I should see "test_user2"


    Scenario: Sent email when resetting password
        Given I have a user in the database:
            | email          | is_active | password                                                                      |
            | user1@test.com | true      | pbkdf2_sha256$36000$gmqHWTUE8h67$SdxOiHl0zlJcMb3lHf+HRCuAP2MqqGtr9QT2oL61wY0= |
        When I visit site page "/password_reset/"
        And I fill in "Email" with "user1@test.com"
        And I press "Reset my password"
        Then I should see "Password reset sent"
        And 1 email has been sent
