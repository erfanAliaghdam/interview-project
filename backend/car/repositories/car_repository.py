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
