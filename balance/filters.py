from django_filters import rest_framework as filters
from rest_framework.pagination import LimitOffsetPagination

from balance.models import Equipment, Charge


class EquipmentFilter(filters.FilterSet):
    created__gte = filters.NumberFilter(field_name='created_by', lookup_expr='gte')
    created__lte = filters.NumberFilter(field_name='created_by', lookup_expr='lte')

    identification = filters.CharFilter(lookup_expr='iexact')

    status = filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Equipment
        fields = (
            'identification',
            'status',
            'created_by'
        )


class EquipmentPagination(LimitOffsetPagination):
    default_limit = 10


class ChargeFilter(filters.FilterSet):
    created__gte = filters.NumberFilter(field_name='created_by', lookup_expr='gte')
    created__lte = filters.NumberFilter(field_name='created_by', lookup_expr='lte')

    identification = filters.CharFilter(lookup_expr='iexact')

    status = filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Charge
        fields = (
            'identification',
            'status',
            'created_by'
        )


class ChargePagination(LimitOffsetPagination):
    default_limit = 10
