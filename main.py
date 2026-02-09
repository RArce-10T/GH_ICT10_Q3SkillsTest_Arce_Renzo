# nested if statement
from pyscript import display, document


def account_authenticator(e):
    document.getElementById('output').innerHTML = " "

    # values
    username = document.getElementById('input1').value
    password = document.getElementById('input2').value
    username_length = len(username)
    password_length = len(password)
    
    # validating informations
    if username_length < 7 and password_length < 10:
           display(f'Your username and password needs more characters.', target='output')
    elif username_length < 7:
           display(f'your username needs more characters.', target='output')
    elif password_length < 7:
           display(f'your password needs more characters.', target='output')
    elif password.isalpha():
        display(f'your password needs letters', target='output')
    elif username.isdigit():
        display(f'your password needs more numbers', target='output')
    else:
         display(f'Greetings, {username}.', target='output')