import pytest

from my_project.calculator import add, divide, multiply, subtract


def test_add(sample_numbers):
    assert add(sample_numbers["a"], sample_numbers["b"]) == 15


def test_subtract(sample_numbers):
    assert subtract(sample_numbers["a"], sample_numbers["b"]) == 5


def test_multiply(sample_numbers):
    assert multiply(sample_numbers["a"], sample_numbers["b"]) == 50


def test_divide(sample_numbers):
    assert divide(sample_numbers["a"], sample_numbers["b"]) == 2


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
