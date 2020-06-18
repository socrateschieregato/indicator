from rest_framework.serializers import ModelSerializer

from balance.models import Equipment, Charge, Weight


class ChargeSerializer(ModelSerializer):
    class Meta:
        model = Charge
        fields = '__all__'


class EquipmentSerializer(ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'


class WeightSerializer(ModelSerializer):
    class Meta:
        model = Weight
        fields = '__all__'
