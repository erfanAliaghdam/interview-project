from rest_framework import serializers
from car.models import Car
from car.repositories import CarRepository
from car.helpers import validate_color_name


class SaleGroupCreateCarSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.repository = CarRepository()

    class Meta:
        model = Car
        fields = [
            "title",
            "description",
            "color",
            "carrying_capacity",
            "cylinder_number",
            "cylinder_capacity"
        ]

    title = serializers.CharField(
        required=True,
        error_messages={
            'required': 'title is required.',
            'invalid': 'title is required.',
        }
    )

    description = serializers.CharField(
        required=True,
        error_messages={
            'required': 'description is required.',
            'invalid': 'description is required.',
        }
    )

    color = serializers.CharField(
        required=True,
        error_messages={
            'required': 'color is required.',
            'invalid': 'color is required.',
        }
    )

    carrying_capacity = serializers.IntegerField(
        required=True,
        error_messages={
            'required': 'carrying capacity is required.',
            'invalid': 'carrying capacity is required.',
        }
    )

    cylinder_number = serializers.IntegerField(
        error_messages={
            'required': 'cylinder number is required.',
            'invalid': 'cylinder number is required.',
        }
    )

    cylinder_capacity = serializers.IntegerField(
        error_messages={
            'required': 'cylinder capacity is required.',
            'invalid': 'cylinder capacity is required.',
        }
    )

    def validate_color(self, color):
        if not validate_color_name(color=color):
            raise serializers.ValidationError("Color is not valid.")
        return color
