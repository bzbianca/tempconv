import pytest
from src.converter import convert, celsius_to_fahrenheit

@pytest.fixture
def freezing_point_c_to_f(freezing_point):
    assert convert(freezing_point['C'], 'C', 'F') == freezing_point['F']


def freezing_point_c_to_k(freezing_point):
    """Returns the freezing point in all three units."""
    assert convert(freezing_point['C'], 'C', 'K') == freezing_point['K']


@pytest.fixture
def boiling_point_f_to_c(boiling_point):
    assert convert(boiling_point['F'], 'F', 'C') == boiling_point['C']

@pytest.mark.parametrize("val, from_u, to_u, expected", [
    (20, "C", "F", 68.0),
    (300, "K", "C", 26.85),
    (50, "F", "C", 10.0),
    (37, "C", "K", 310.15)
])
def test_conversions(val, from_u, to_u, expected):
    assert convert(val, from_u, to_u) == pytest.approx(expected)


def test_convert_same_unit():
    assert convert(25.0, 'C', 'C') == 25.0


def test_unknown_unit_raises_error():
    with pytest.raises(ValueError):
        convert(100, 'C', 'X')


def test_negative_kelvin_raises_error():
    with pytest.raises(ValueError):
        convert(-1.0, 'K', 'C')


def test_below_absolute_zero_raises_error():
    with pytest.raises(ValueError):
        convert(-274.0, 'C', 'K')

@pytest.mark.edge
def test_absolute_zero_boundary():
    assert convert(-273.15, 'C', 'K') == 0.0

def test_direct_c_to_f():
    assert celsius_to_fahrenheit(0) == 32.0
