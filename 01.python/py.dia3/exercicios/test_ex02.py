import pytest
from ex02 import expression_to_number


def test_expression_to_number_returns_expected():
    assert expression_to_number("1-HOME-SWEET-HOME") == "1-4663-79338-4663"


def test_expression_to_number_returns_empty():
    assert expression_to_number("") == ""


def test_expression_to_number_raises_exception():
    with pytest.raises(
        TypeError, match="missing 1 required positional argument: 'exp'"
    ):
        expression_to_number()


def test_expression_to_number_with_long_string():
    string = "The quick brown fox jumps over the lazy dog-The quick brown fox"
    result = "843 78425 27696 369 58677 6837 843 5299 364-843 78425 27696 369"
    assert expression_to_number(string) == result
