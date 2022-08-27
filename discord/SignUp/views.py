from django.http import HttpResponse
from django.shortcuts import render
from .forms import SignUpForm
from .models import SignUp
import datetime
import json

# Create your views here.
year_seq = [str(i) for i in range(int(datetime.datetime.now().year) - 1, int(datetime.datetime.now().year) - 130, -1)]
month_seq = ['January', 'February', 'March', 'April', 'May', 'June',
             'July', 'August', 'September', 'October', 'November', 'December']
day_seq = [str(i) for i in range(1, 32)]


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if request.POST.get('password') != request.POST.get('confirm_password'):
            form.add_error('confirm_password', 'Passwords do not match')
        if form.is_valid():
            y, m, d = int(request.POST['birth_year']),\
                      month_seq.index(request.POST.get('birth_month')) + 1,\
                      int(request.POST.get('birth_day'))
            birth_date = datetime.datetime.date(datetime.datetime(y, m, d))
            form.save()
            SignUp.objects.filter(username=form.cleaned_data['username']).update(birth_date=birth_date)
            return HttpResponse('<h1>successful<h1>')
        errors = {}
        for field in form.fields:
            if len(form[field].errors) > 0:
                errors[field] = str(form[field].errors[0])
        errors = json.dumps(errors)

        return render(request, 'SignUp/SignUp.html', {'form': form, 'year_seq': year_seq, 'month_seq': month_seq,
                                                      'day_seq': day_seq, 'errors': errors})
    form = SignUpForm()
    errors = json.dumps({})
    return render(request, 'SignUp/SignUp.html', {'form': form, 'year_seq': year_seq, 'month_seq': month_seq,
                                                  'day_seq': day_seq, 'errors': errors})
