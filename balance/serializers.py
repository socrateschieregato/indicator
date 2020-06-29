from rest_framework.serializers import ModelSerializer

from balance.models import Equipment, Charge, Weight


class EquipmentSerializer(ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['identification']


class WeightSerializer(ModelSerializer):
    class Meta:
        model = Weight
        fields = '__all__'


class ChargeSerializer(ModelSerializer):
    equipment = EquipmentSerializer(many=False)
    weight = WeightSerializer(many=False)

    class Meta:
        model = Charge
        fields = '__all__'
