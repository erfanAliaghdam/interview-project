from rest_framework import serializers

from car.models import Car
from car.repositories import CarRepository


class SaleGroupDetailCarSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.repository = CarRepository()

    class Meta:
        model = Car
        fields = [
            "id",
            "title",
            "description",
            "color",
            "carrying_capacity",
            "cylinder_number",
            "cylinder_capacity"
        ]
