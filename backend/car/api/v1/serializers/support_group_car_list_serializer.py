from rest_framework import serializers
from car.models import Car


class SupportCarListSerializer(serializers.ModelSerializer):
    owner_name = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = [
            "title",
            "color",
            "carrying_capacity",
            "cylinder_number",
            "cylinder_capacity",
            "engine_capacity",
            "owner_name"
        ]

    def get_owner_name(self, car):
        car.owner.get_full_name()
