from django_filters import rest_framework as filters
from rest_framework.pagination import LimitOffsetPagination

from balance.models import Equipment, Charge, Weight


class EquipmentFilter(filters.FilterSet):
    created__gte = filters.NumberFilter(field_name='created_at', lookup_expr='gte')
    created__lte = filters.NumberFilter(field_name='created_at', lookup_expr='lte')

    identification = filters.CharFilter(lookup_expr='iexact')

    status = filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Equipment
        fields = (
            'identification',
            'status',
            'created_at'
        )


class EquipmentPagination(LimitOffsetPagination):
    default_limit = 10


class ChargeFilter(filters.FilterSet):
    created__gte = filters.NumberFilter(field_name='created_at', lookup_expr='gte')
    created__lte = filters.NumberFilter(field_name='created_at', lookup_expr='lte')

    identification = filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Charge
        fields = (
            'identification',
            'created_at'
        )


class ChargePagination(LimitOffsetPagination):
    default_limit = 10


class WeightFilter(filters.FilterSet):
    created__gte = filters.NumberFilter(field_name='created_at', lookup_expr='gte')
    created__lte = filters.NumberFilter(field_name='created_at', lookup_expr='lte')

    created_by = filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Weight
        fields = (
            'created_by',
            'created_at'
        )


class WeightPagination(LimitOffsetPagination):
    default_limit = 10
