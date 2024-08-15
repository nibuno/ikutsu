from .views import calc_age

def test_calc_age(freezer):
    # FIXME: アサーションルーレットになっているので修正
    freezer.move_to("2024-02-21")
    assert calc_age(birth_date_year=1993, birth_date_month=2, birth_date_day=20) == 30
    assert calc_age(birth_date_year=1993, birth_date_month=2, birth_date_day=21) == 31
