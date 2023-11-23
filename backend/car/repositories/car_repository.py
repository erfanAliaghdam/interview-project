from django.db import transaction
from car.models import Car
from django_elasticsearch_dsl.search import Search


class CarRepository:
    def __init__(self):
        self.elastic = Search(index='cars')

    def get_all_cars(self):
        return Car.objects.all()

    def get_all_cars_and_owner_details(self):
        return self.get_all_cars().select_related("owner")

    def search_cars(
            self,
            search_term: str,
            color: str = None,
            cylinder_number: str = None,
            owner_name: str = None
    ):
        query = self.elastic
        if search_term:
            query = query.query(
                "multi_match", query=search_term, fields=[
                    'title',
                    'description'
                ]
            )

        if color:
            query = query.filter("term", color=color)
        if cylinder_number:
            query = query.filter("term", cylinder_number=cylinder_number)
        if owner_name:
            query = query.filter("match", owner_full_name=owner_name)

        query = query.extra(size=10000)
        cars = query.execute()

        return cars

    def get_car_by_id(self, car_id: int):
        return Car.objects.filter(
            pk=car_id
        )

    def check_if_car_exists_by_car_id(self, car_id: int) -> bool:
        car = self.get_car_by_id(car_id=car_id)
        if not car.exists():
            return False
        return True

    @transaction.atomic
    def update_car_info_by_car_id(
            self,
            car_id: int,
            color: str,
            title: str,
            description: str,
            carrying_capacity: int,
            cylinder_number: int,
            cylinder_capacity: int
    ):
        car = self.get_car_by_id(car_id=car_id).select_for_update().first()
        car.color = color
        car.title = title
        car.description = description
        car.carrying_capacity = carrying_capacity
        car.cylinder_number = cylinder_number
        car.cylinder_capacity = cylinder_capacity
        car.save()

        return car

    def create_car(
            self,
            color: str,
            title: str,
            description: str,
            carrying_capacity: int,
            cylinder_number: int,
            cylinder_capacity: int,
            owner_id: str
    ):
        car = Car.objects.create(
            color=color,
            title=title,
            description=description,
            carrying_capacity=carrying_capacity,
            cylinder_number=cylinder_number,
            cylinder_capacity=cylinder_capacity,
            owner_id=owner_id
        )
        return car
