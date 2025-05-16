"""Tests for `sahlas_python_course_demo_05_16_2025.states_info`."""

import pytest

from sahlas_python_course_demo_05_16_2025.states_info import (
    is_city_capitol_of_state,
    slow_add,
)


@pytest.mark.parametrize(
    argnames=("city_name", "state", "is_capitol"),
    argvalues=[
        ("Montgomery", "Alabama", True),
        ("Oklahoma City", "Oklahoma", True),
        ("Salem", "Oregon", True),
        ("Salt Lake City", "Alabama", False),
    ],
)
def test__is_city_capitol_of_state(city_name: str, state: str, is_capitol: bool):
    """Assert `is_city_capitol_of_state()`."""
    assert is_city_capitol_of_state(city_name=city_name, state=state) == is_capitol


@pytest.mark.slow
def test__slow_add():
    """Assert `slow_add()`."""
    assert slow_add(1, 2) == 3
