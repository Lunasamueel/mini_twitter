from django.urls import path
from register.views import RegistrationView

urlpatterns = [
    path('', RegistrationView.as_view(), name='register'),
]