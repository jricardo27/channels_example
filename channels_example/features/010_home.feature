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


    Scenario: Connect websocket
        When I visit site page "/"
        And I press "Connect"
        Then I should see "connected"
