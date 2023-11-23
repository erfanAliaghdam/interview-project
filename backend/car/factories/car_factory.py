from car.models import Car
import factory


class CarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Car

    title = factory.Sequence(lambda n: f'car - {n}')
    description = factory.Faker('sentence')
    color = factory.Faker(
        'random_element',
        elements=[choice[0] for choice in Car.COLOR_CHOICES]
    )
    carrying_capacity = factory.Faker('random_int', min=1, max=24)
    cylinder_number = factory.Faker('random_int', min=1, max=16)
    cylinder_capacity = factory.Faker('random_int', min=50, max=660)
