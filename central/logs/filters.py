from django_filters import rest_framework as filter
from .models import Log
class LogFilterSet(filter.FilterSet):
    class Meta:
        model = Log
        fields = (
            'title',
            'archived',
            'events',
            'level',
            'origin',
            'env'
        )