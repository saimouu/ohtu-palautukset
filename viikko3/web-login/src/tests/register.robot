*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  janne
    Set Password  janne123
    Set Password Confirmation  janne123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ja
    Set Password  ja12345678
    Set Password Confirmation  ja12345678
    Submit Credentials
    Register Should Fail With Message  Username must be atleast 3 characters long and contain only characters from a-z


Register With Valid Username And Too Short Password
    Set Username  jaakko
    Set Password  ok 
    Set Password Confirmation  ok 
    Submit Credentials
    Register Should Fail With Message  Password must contain atleast 8 characters and include other characters than just letters

Register With Valid Username And Invalid Password
    Set Username  pekka 
    Set Password  pekkapekkapekka 
    Set Password Confirmation  pekkapekkapekka 
    Submit Credentials
    Register Should Fail With Message  Password must contain atleast 8 characters and include other characters than just letters

Register With Nonmatching Password And Password Confirmation
    Set Username  pekka 
    Set Password  pekkapekkapekka123 
    Set Password Confirmation  jotain 
    Submit Credentials
    Register Should Fail With Message  Passwords do not match 

Register With Username That Is Already In Use
    Set Username  kalle 
    Set Password  kalle54321 
    Set Password Confirmation  kalle54321
    Submit Credentials
    Register Should Fail with Message  User with username kalle already exists

Login After Successful Registration
    Set Username  tyyppi 
    Set Password  tyyppi123 
    Set Password Confirmation  tyyppi123
    Submit Credentials
    Go To Main Page
    Click Button  Logout
    Set Username  tyyppi 
    Set Password  tyyppi123 
    Click Button  Login
    Main Page Should Be Open 
    
    
Login After Failed Registration
    Set Username  tyyppi1 
    Set Password  tyyppi123
    Set Password Confirmation  tyyppi123
    Submit Credentials
    Go To Login Page
    Set Username  tyyppi1 
    Set Password  tyyppi123 
    Click Button  Login
    Page Should Contain  Invalid username or password


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register 

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}


Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
