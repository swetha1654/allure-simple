import pytest

from my_project.utils import is_even, is_odd


@pytest.mark.parametrize(
    "number, expected", [(2, True), (3, False), (10, True), (7, False)]
)
def test_is_even(number, expected):
    assert is_even(number) == expected


@pytest.mark.parametrize(
    "number, expected", [(2, False), (3, True), (10, False), (7, True)]
)
def test_is_odd(number, expected):
    assert is_odd(number) == expected


def test_is_even_with_fixture(sample_list):
    for num in sample_list:
        assert is_even(num) == (num % 2 == 0)
