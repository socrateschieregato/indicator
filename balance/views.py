from rest_framework import viewsets

from balance import filters
from balance.filters import ChargeFilter, EquipmentFilter, ChargePagination, EquipamentPagination
from balance.models import Equipment, Charge
from balance.serializers import EquipmentSerializer, ChargeSerializer


class ReceiptViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = EquipmentFilter
    pagination_class = EquipmentPagination

    def filter_queryset(self, queryset):
        queryset = super(ReceiptViewSet, self).filter_queryset(queryset)
        return queryset.order_by('-created_at',)


class ChargeViewSet(viewsets.ModelViewSet):
    queryset = Charge.objects.all()
    serializer_class = ChargeSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ChargeFilter
    pagination_class = ChargePagination

    def filter_queryset(self, queryset):
        queryset = super(ReceiptViewSet, self).filter_queryset(queryset)
        return queryset.order_by('-created_at',)
