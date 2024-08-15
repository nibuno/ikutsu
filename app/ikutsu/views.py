from django.shortcuts import render

from django.views import View
from ikutsu.forms import AgeForm

from datetime import date


class IndexView(View):
    form_class = AgeForm
    template_name = 'index.html'

    def get (self, request):

        if not request.GET:
            form = self.form_class()
            return render(request, self.template_name, {'form': form})

        form = self.form_class(request.GET)
        if not form.is_valid():
            return render(request, self.template_name, {'form': form})

        my_birth_date_year = form.cleaned_data['my_birth_date'].year
        my_birth_date_month = form.cleaned_data['my_birth_date'].month
        my_birth_date_day = form.cleaned_data['my_birth_date'].day

        age = calc_age(my_birth_date_year, my_birth_date_month, my_birth_date_day)

        return render(request, 'index.html', {'form': form, 'age': age})


def calc_age(birth_date_year: int, birth_date_month: int, birth_date_day: int) -> int:
    """年齢を計算する"""

    today = date.today()

    birth_date = date(birth_date_year, birth_date_month, birth_date_day)

    age = today.year - birth_date.year

    # 誕生日がまだ来ていない場合、年齢を1つ減らす
    if (today.month, today.day) > (birth_date.month, birth_date.day):
        age -= 1

    return age
