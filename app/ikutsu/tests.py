import pytest

from .views import calc_age

@pytest.mark.parametrize(
    "birth_date_year, birth_date_month, birth_date_day, move_to_date, expected",
    [
        (1993, 2, 20, '2024-02-21', 30),
        (1993, 2, 21, '2024-02-21', 31),
        (1993, 2, 21, '2024-08-15', 31),
    ]
)
def test_calc_age(freezer, birth_date_year, birth_date_month, birth_date_day, move_to_date, expected):
    # arrange
    freezer.move_to(move_to_date)

    # act
    actual = calc_age(birth_date_year, birth_date_month, birth_date_day)
    expected = expected

    # assert
    assert actual == expected
