# Name: Jennifer Daniels
# Assignment: TDD Hands On
# Description: Program performs several test to check if the program
# check_pwd.py is operating correctly


import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):
    """
    Class includes test to check the requirements for a password including:
    Must be between 8 and 20 characters (inclusive)
    Must contain at least one lowercase letter
    Must contain at least one uppercase letter
    Must contain at least one digit
    Must contain at least one symbol from: ~`!@#$%^&*()_+-=
    """

    def test1(self):
        # test for password with letters only and length 8
        # Checking correct length with a string should return true
        assert_input = "Abcdef!1"
        self.assertTrue(check_pwd(assert_input),
                         msg='check_pwd()'.format())

    def test2(self):
        # test for password with empty string
        # Checking empty string should return false
        assert_input = ""
        self.assertFalse(check_pwd(assert_input),
                        msg='check_pwd()'.format())

    def test3(self):
        # test for password with correct characters length of 7
        # Checking to make sure test fails for length less than 8
        assert_input = "Abcdf!1"
        self.assertFalse(check_pwd(assert_input),
                         msg='check_pwd()'.format())

    def test4(self):
        # test for password with correct characters length of 21
        # Checking to make sure test fails for length more than 20
        assert_input = "Abcdf!1jtrefirtydflqr"
        self.assertFalse(check_pwd(assert_input),
                         msg='check_pwd()'.format())

    def test5(self):
        # test for password with incorrect characters length of 8
        # Checking to make sure test fails for no lowercase letter
        assert_input = "ABCDEF!1"
        self.assertFalse(check_pwd(assert_input),
                         msg='check_pwd()'.format())

    def test6(self):
        # test for password with incorrect characters length of 8
        # Checking to make sure test fails for no uppercase letter
        assert_input = "abcdfg!1"
        self.assertFalse(check_pwd(assert_input),
                         msg='check_pwd()'.format())

    def test7(self):
        # test for password with correct characters length of 8
        # Checking to make sure test fails for no number
        assert_input = "abcdfH!a"
        self.assertFalse(check_pwd(assert_input),
                         msg='check_pwd()'.format())

    def test8(self):
        # test for password with correct characters length of 8
        # Checking to make sure test pass for correct character ~
        assert_input = "abcdfHa~"
        self.assertFalse(check_pwd(assert_input),
                         msg='check_pwd()'.format())

    def test9(self):
        # test for password with correct characters length of 8
        # Checking to make sure test pass for correct character `
        assert_input = "abcdfHa`"
        self.assertFalse(check_pwd(assert_input),
                         msg='check_pwd()'.format())

    def test10(self):
        # test for password with correct characters length of 8
        # Checking to make sure test pass for correct character `
        assert_input = "abcdfH!@"
        self.assertFalse(check_pwd(assert_input),
                         msg='check_pwd()'.format())



if __name__ == '__main__':
    unittest.main()