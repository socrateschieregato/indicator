from django_filters import rest_framework as filters
from rest_framework import viewsets, status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from balance.filters import ChargeFilter, EquipmentFilter, ChargePagination, EquipmentPagination, WeightFilter, \
    WeightPagination
from balance.models import Equipment, Charge, Weight
from balance.serializers import EquipmentSerializer, ChargeSerializer, WeightSerializer
from balance.tasks import read_weight_by_serial_port


class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = EquipmentFilter
    pagination_class = EquipmentPagination
    lookup_field = 'identification'

    def filter_queryset(self, queryset):
        queryset = super(EquipmentViewSet, self).filter_queryset(queryset)
        return queryset.order_by('-created_at',)


class ChargeViewSet(viewsets.ModelViewSet):
    queryset = Charge.objects.all()
    serializer_class = ChargeSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ChargeFilter
    pagination_class = ChargePagination

    def retrieve(self, request, *args, **kwargs):
        weight = read_weight_by_serial_port()
        if weight >= 0:
            return Response(data=weight, status=200)
        raise NotFound

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def filter_queryset(self, queryset):
        queryset = super(ChargeViewSet, self).filter_queryset(queryset)
        return queryset.order_by('-created_at',)


class WeightAPIView(viewsets.ModelViewSet):
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = WeightFilter
    pagination_class = WeightPagination

    def filter_queryset(self, queryset):
        queryset = super(WeightAPIView, self).filter_queryset(queryset)
        return queryset.order_by('-created_at',)
