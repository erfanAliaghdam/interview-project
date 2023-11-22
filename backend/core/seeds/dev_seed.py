from random import randint
from django.conf import settings
from django.contrib.auth import get_user_model
from car.models import Car
from users.factories import UserFactory, GroupFactory
from car.factories import CarFactory


def generate_development_seed():
    superuser_email = "superuser@example.com"
    superuser_password = "DefaultPassword"
    get_user_model().objects.create_superuser(
        email=superuser_email,
        password=superuser_password
    )
    print("!!! superuser email for development environment: ", superuser_email, " !!!")
    print("!!! superuser superuser_password for development environment: ",
          superuser_password, " !!!")
    groups_list = settings.GROUP_LIST
    for group in groups_list:
        GroupFactory.create(name=group)
    client_users = UserFactory.create_batch(500, assign_to_group="Client")
    UserFactory.create_batch(20, assign_to_group="Support")
    UserFactory.create_batch(20, assign_to_group="Sale")
    for client in client_users:
        number_of_owned_cars = randint(1, 6)
        CarFactory.create_batch(number_of_owned_cars, owner=client)
    UserFactory.create_batch(12, is_staff=True)

    print(str(get_user_model().objects.all().count()), "users created. ")
    print(str(Car.objects.all().count()), "cars created. ")
