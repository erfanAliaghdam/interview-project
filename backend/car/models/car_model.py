from django.contrib.auth import get_user_model
from django.db import models
from car.helpers import get_color_names_choice_tuple


class Car(models.Model):
    COLOR_CHOICES = get_color_names_choice_tuple()
    title = models.CharField(max_length=255)
    description = models.TextField()
    color = models.CharField(choices=COLOR_CHOICES, max_length=255)
    carrying_capacity = models.PositiveSmallIntegerField()
    cylinder_number = models.PositiveSmallIntegerField()
    cylinder_capacity = models.PositiveSmallIntegerField()
    owner = models.ForeignKey(
        get_user_model(),
        related_name="cars",
        on_delete=models.RESTRICT
    )

    @property
    def engine_capacity(self):
        return self.cylinder_number * self.cylinder_capacity
