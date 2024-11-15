from django.urls import path

from .views import *


urlpatterns = [
    path('', (AdList.as_view()), name='ads_list'),
    path('<int:pk>', (AdDetail.as_view()), name='ad_detail'),
    path('create/', (AdCreate.as_view()), name='ad_create'),
    path('<int:pk>/update/', (AdUpdate.as_view()), name='ad_update'),
    path('<int:pk>/delete/',(AdDelete.as_view()), name='ad_delete'),
    path('<int:pk>/response/create/', (UserResponseCreate.as_view()), name='user_response_create'),
    path('responses/', (UserResponseList.as_view()), name='responses_list'),
    path('responses/<int:pk>/delete/', (UserResponseDelete.as_view()), name='response_delete'),
    path('profile/', (ProfileFilter.as_view()), name='profile'),
    path('<int:pk>/response/confirm/', confirm_response, name='confirm_response'),
]
