from django.urls import path

from .views import confirm_user


urlpatterns = [
    path('confirm/', confirm_user, name='confirm_user'),
]
