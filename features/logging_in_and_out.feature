Feature: Logging in and out
In order to log in and out,
the user needs to visit the 
log in and log out pages.

Scenario: I'm logged out
    When I log out
    Then There is no "Log out" link
    And There is a "Sign in" link
    And There is a "Register" link

Scenario: I'm logged in
    Given User "user1" with password "alskj1234" exists
    And I am not logged in
    When I log in as user "user1" with password "alskj1234"
    And I go to the home page
    Then There is a "Login" link

