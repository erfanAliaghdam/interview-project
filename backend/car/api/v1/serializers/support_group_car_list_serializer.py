from rest_framework import serializers
from car.models import Car


class SupportCarListSerializer(serializers.ModelSerializer):
    owner_full_name = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = [
            "id",
            "title",
            "color",
            "carrying_capacity",
            "cylinder_number",
            "cylinder_capacity",
            "engine_capacity",
            "owner_full_name"
        ]

    def get_owner_full_name(self, car):
        return car.owner_full_name

