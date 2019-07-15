"""
The following things should trigger an error:

The user leaves any of the following fields empty: username, password, verify password.

The user's username or password is not valid -- for example, it contains a space character or it consists of less than 3 characters
or more than 20 characters (e.g., a username or password of "me" would be invalid).

The user's password and password-confirmation do not match.

The user provides an email, but it's not a valid email.
Note: the email field may be left empty, but if there is content in it, then it must be validated.
The criteria for a valid email address in this assignment are that it has a single @, a single ., contains no spaces, and is between 3 and 20 characters long.

Each feedback message should be next to the field that it refers to.

For the username and email fields, you should preserve what the user typed, so they don't have to retype it.
With the password fields, you should clear them, for security reasons.
"""

def valid_username(username):
    """checks validity of given username"""
    return False if len(username) < 3 or len(username) > 20 or " " in username else return True

def passwords_match(password, passconfirm):
    """compares password and password confirmation to check for equality"""
    return True if password == passconfirm else return False

def valid_email(email):
    """checks validity of given email address"""
    valid = True
    if len(email) < 3 or len(email) > 20:
        valid = False
    elif "@" not in email or "." not in email:
        valid = False
    elif " " in email:
        valid = False
    