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
    # checks to see if password has a lowercase letter
    symbols = '~`!@#$%^&*()_+-='
    check_l = False  # bool for lowercase
    check_u = False  # bool for uppercase
    check_n = False  # bool for number
    check_s = False
    for i in pss_wrd:
        asc_conv = ord(i)
        if 96 < asc_conv < 123:  # checks for lowercase letters
            check_l = True
        elif 64 < asc_conv < 91:  # checks for uppercase letters
            check_u = True
        elif 47 < asc_conv < 58:  # checks for numbers 0 - 9
            check_n = True
        elif i in symbols:  # checks for correct symbols
            check_s = True
        else:
            return False
    if not check_l or not check_u or not check_n or not check_s:
        return False
    return check_p
