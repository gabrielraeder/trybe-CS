from ex04 import list_email_check


def test_if_doesnt_have_emails_returns_empty_list():
    assert list_email_check([]) == []


def test_only_valid_emails():
    emails = ["username@website.com"]
    expected_emails = ["username@website.com"]
    assert list_email_check(emails) == expected_emails


def test_invalid_emails_should_be_filtered():
    emails = ["user#ame@website.com"]
    expected_emails = []
    assert list_email_check(emails) == expected_emails


def test_valid_and_invalid_emails_returns_only_valids():
    emails = ["username@website.com", "user#ame@website.com"]
    expected_emails = ["username@website.com"]
    assert list_email_check(emails) == expected_emails
