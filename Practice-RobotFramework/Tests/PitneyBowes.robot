*** Settings ***

Documentation  This is some basic information about the whole suit
Library  Selenium2Library
Library  OperatingSystem



*** Variables ***

*** Test Cases ***

User must sign in to check out

    [Documentation]  This is some basic information about the test
    [Tags]  Smoke
    Open Browser  https://www.pitneybowes.com/in  chrome
    sleep  5s
    Click Element  xpath=//h2[text()="Customer Engagement"]
    sleep  5s
    Click Element  xpath=//h1[2]
    sleep  3s
    Close Browser

*** Keywords ***