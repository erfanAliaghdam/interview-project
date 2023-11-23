from django.urls import path
from car.api.v1.views import (
    support_group_car_list_view,
    sale_group_car_update_view
)


urlpatterns = [
    path("support/cars/", support_group_car_list_view, name="support-car-list"),
    path("sale/cars/<int:car_id>", sale_group_car_update_view, name="sale-car-update")
]
