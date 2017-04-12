Feature: Test home page

    Scenario: See "Hello World"
        When I visit site page "/"
        Then I should see "Hello World"
