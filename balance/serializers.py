from rest_framework.serializers import ModelSerializer

from balance.models import Equipment, Charge


class EquipmentSerializer(ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'


class ChargeSerializer(ModelSerializer):
    class Meta:
        model = Charge
        fields = '__all__'
