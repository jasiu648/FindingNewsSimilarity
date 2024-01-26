# test_speed.py
import pytest

@pytest.mark.benchmark(min_rounds=5)
def test_speed():
    result = sum(range(1000000))
    assert result is not None

