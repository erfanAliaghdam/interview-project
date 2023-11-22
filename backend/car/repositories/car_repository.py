from car.models import Car


class CarRepository:
    def __init__(self):
        pass

    def get_all_cars(self):
        return Car.objects.all()

    def get_all_cars_and_owner_details(self):
        return self.get_all_cars().select_related("owner")
