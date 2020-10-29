import pytest


def func(x):
    pytest.set_trace()

    return x + 1


def test_answer():
    pytest.set_trace()

    assert func(3) == 5