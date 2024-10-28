from django.urls import path

from .views import *

urlpatterns = [
    path('', (AdList.as_view()), name='ads_list'),
    path('<int:pk>', (AdDetail.as_view()), name='ad_detail'),
    path('create/', (AdCreate.as_view()), name='ad_create'),
    path('<int:pk>/update/', (AdUpdate.as_view()), name='ad_update'),
    path('<int:pk>/delete/',(AdDelete.as_view()), name='ad_delete'),
]