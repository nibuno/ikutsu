import pytest

from .views import calc_age

@pytest.mark.parametrize(
    "birth_date_year, birth_date_month, birth_date_day, expected",
    [
        (1993, 2, 20, 30),
        (1993, 2, 21, 31),
    ]
)
def test_calc_age(freezer, birth_date_year, birth_date_month, birth_date_day, expected):
    # arrange
    freezer.move_to("2024-02-21")

    # act
    actual = calc_age(birth_date_year, birth_date_month, birth_date_day)
    expected = expected

    # assert
    assert actual == expected
