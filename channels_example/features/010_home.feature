Feature: Test home page

    Scenario: Get time from server.
        Given today's date is 1804-02-29 and time is 15:24h
        When I visit site page "/"
        Then I should see "It was 1804-02-29 15:24:00.000000 on the server when this page was loaded."
