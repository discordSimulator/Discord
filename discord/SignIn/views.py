from django.http import HttpResponse
from django.shortcuts import render
from SignUp.models import SignUp

# Create your views here.


def sign_in(request):
    if request.method == "POST":
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')
        if SignUp.objects.filter(username=username_or_email).exists() or\
                SignUp.objects.filter(email=username_or_email).exists():
            if SignUp.objects.filter(password=password).exists():
                return HttpResponse('User {} successfully signed in'.format(username_or_email))
            error = "Incorrect password"
            return render(request, 'SignIn/SignIn.html', {'error': error})
        error = "Incorrect username or email"
        return render(request, 'SignIn/SignIn.html', {'error': error})
    return render(request, 'SignIn/SignIn.html', {'error': ""})
