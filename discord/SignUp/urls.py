from django.urls import path
from . import views

urlpatterns = [
    path('SignUp/', views.sign_up)
]