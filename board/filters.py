import django_filters
from django_filters import FilterSet
from django.forms import DateTimeInput

from .models import UserResponse


class AuthorProfileFilter(FilterSet):
    after_add = django_filters.DateTimeFilter(
        field_name='creation_time',
        lookup_expr='gt',
        label='Опубликованы позднее чем',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'}
        )
    )    
    
    class Meta:
        model = UserResponse
        label='Объявления'
        fields = {
            'ad': ['exact'],
       }
