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

    check_p = True
    # checks that length of string is between 8 and 20
    if len(pss_wrd) < 8 or len(pss_wrd) > 20:
        return False

    # checks to see if password has a lowercase letter
    check_l = False  # bool for lowercase
    check_u = False  # bool for uppercase
    check_n = False  # bool for number
    for i in pss_wrd:
        if i.islower():
            check_l = True
        if i.isupper():
            check_u = True
        if i.isnumeric():
            check_n = True
    if not check_l or not check_u or not check_n:
        return False
    return check_p
