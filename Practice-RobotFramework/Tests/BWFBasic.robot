*** Settings ***

Documentation  This is some basic information about the whole suit
Library  Selenium2Library
Library  OperatingSystem



*** Variables ***

*** Test Cases ***

User must sign in to check out

    [Documentation]  This is some basic information about the test
    [Tags]  Smoke
    Open Browser  http://www.bwfbadminton.com  chrome
    sleep  5s
    Close Browser

*** Keywords ***