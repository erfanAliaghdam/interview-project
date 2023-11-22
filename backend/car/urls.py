from django.urls import path
from car.api.v1.views import support_group_car_list_view


urlpatterns = [
    path("support/cars/", support_group_car_list_view, name="support-car-list")
]
