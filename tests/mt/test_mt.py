"""Tests for Mersenne Twister implementation."""

import os

import pytest

from algos.mt import randint32


def test_is_random() -> None:
    """Test that the generator is random."""
    a, b = randint32(), randint32()
    x = list(next(a) for _ in range(1_000))
    y = list(next(b) for _ in range(1_000))

    assert x != y


def test_is_deterministic() -> None:
    """Test that the generator is deterministic."""
    seed = list(range(624))
    a, b = randint32(seed), randint32(seed)
    x = list(next(a) for _ in range(1_000))
    y = list(next(b) for _ in range(1_000))

    assert x == y
