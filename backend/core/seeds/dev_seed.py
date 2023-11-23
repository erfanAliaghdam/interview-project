from random import randint
from django.conf import settings
from django.contrib.auth import get_user_model
from car.models import Car
from users.factories import UserFactory, GroupFactory
from car.factories import CarFactory


def generate_development_seed():
    superuser_email = "superuser@example.com"
    default_password = "DefaultPassword"
    get_user_model().objects.create_superuser(
        email=superuser_email,
        password=default_password
    )
    print("!!! superuser email for development environment: ", superuser_email, " !!!")
    print("!!! superuser password for development environment: ",
          default_password, " !!!")
    print("\n wait .....")
    groups_list = settings.GROUP_LIST
    for group in groups_list:
        GroupFactory.create(name=group)
    UserFactory.create_batch(10, assign_to_group="Client")
    UserFactory.create_batch(20, assign_to_group="Support")
    sale_group_users = UserFactory.create_batch(100, assign_to_group="Sale")
    for user in sale_group_users:
        number_of_owned_cars = randint(1, 50)
        CarFactory.create_batch(number_of_owned_cars, owner=user)

    support_user = UserFactory.create(
        assign_to_group="Support",
        email="support@example.com"
    )
    seller_user = UserFactory.create(
        assign_to_group="Sale",
        email="seller@example.com"

    )
    support_user.set_password(default_password)
    seller_user.set_password(default_password)
    support_user.save()
    seller_user.save()

    print(
        "!!! support user email for development environment: ",
        support_user.email,
        " !!!"
    )
    print(
        "!!! support user password for development environment: ",
        default_password,
        " !!!"
    )
    print(
        "!!! seller email for development environment: ",
        seller_user.email,
        " !!!"
    )
    print(
        "!!! seller password for development environment: ",
        default_password,
        " !!!"
    )
    print(str(get_user_model().objects.all().count()), "users created. ")
    print(str(Car.objects.all().count()), "cars created. ")
