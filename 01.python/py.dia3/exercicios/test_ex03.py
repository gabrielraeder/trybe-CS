from pytest import raises
from ex03 import email_check


def test_email_check_with_valid():
    assert email_check("gabriel_@hotmail.com") is True


def test_email_check_with_invalid_first_character():
    with raises(ValueError, match="Must start with character!"):
        email_check("1abriel@hotm.com")


def test_email_check_with_invalid_username():
    with raises(ValueError, match="Invalid character!"):
        email_check("gabr$el@hotm.com")


def test_email_check_with_invalid_website():
    with raises(ValueError, match="Invalid website!"):
        email_check("gabriel@ho$m.com")


def test_email_check_with_invalid_extension():
    with raises(ValueError, match="Invalid extension!"):
        email_check("gabriel@hotm.coom")
