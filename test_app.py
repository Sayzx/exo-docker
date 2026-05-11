"""Tests pour app.py."""
import pytest
from app import add, multiply, greet


def test_add():
    """Test additionner."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_multiply():
    """Test multiplier."""
    assert multiply(2, 3) == 6
    assert multiply(0, 100) == 0


def test_greet():
    """Test saluer."""
    assert greet("Alice") == "Bonjour, Alice!"
    assert greet("Bob") == "Bonjour, Bob!"
