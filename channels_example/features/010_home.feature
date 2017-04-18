Feature: Test home page

    Scenario: See "Hello World"
        When I visit site page "/"
        Then I should see "Hello World"
        And I should see "The are no registered users."


    Scenario: See list of users:
        Given I have a user in the database:
            | username   |
            | test_user1 |
            | test_user2 |
        When I visit site page "/"
        Then I should see "List of users:"
        And I should see "test_user1"
        And I should see "test_user2"


    Scenario: Get time from server.
        Given today's date is 1804-02-29 and time is 15:24h
        When I visit site page "/"
        Then I should see "It was 1804-02-29 15:24:00.000000 on the server when this page was loaded."
