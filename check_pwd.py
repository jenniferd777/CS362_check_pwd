# Jennifer Daniels
# Assignment: TDD Hands On
# Description: Program performs several test to check if the program
# check_pwd.py is operating correctly


def check_pwd(pss_wrd):
    """
    Program checks password to meet requirements including:
    Must be between 8 and 20 characters (inclusive)
    Must contain at least one lowercase letter
    Must contain at least one uppercase letter
    Must contain at least one digit
    Must contain at least one symbol from: ~`!@#$%^&*()_+-=
    """

    check_p = False
    if len(pss_wrd) > 7 or len(pss_wrd) < 21:
        check_p = True
    for i in pss_wrd:
        check_p = False
        if i.islower():
            check_p = True
            break
    return check_p
