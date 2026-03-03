import pytest
from src.package_sort import PackageCategory, sort


@pytest.mark.parametrize("w, h, l, m, expected", [
    (10, 10, 10, 5, PackageCategory.STANDARD),
    (150, 10, 10, 5, PackageCategory.SPECIAL),
    (200, 200, 200, 50, PackageCategory.REJECTED),
    (200, 200, 201, 50, PackageCategory.REJECTED),
])
def test_sort(w, h, l, m, expected):
    assert sort(w, h, l, m) == expected


def test_sort_negative_weight():
    with pytest.raises(ValueError):
        sort(10, 10, 10, -5)


def test_sort_invalid_size():
    with pytest.raises(ValueError):
        sort(10, 10, 0, 20)
