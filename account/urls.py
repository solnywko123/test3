from django.urls import path
from .views import sign_up, sign_in

urlpatterns = [
    path('signup/', sign_up),
    path('signin/', sign_in),
]