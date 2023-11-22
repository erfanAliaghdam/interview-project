from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from users.factories import UserFactory, GroupFactory


def generate_development_seed():
    superuser_email = "superuser@example.com"
    get_user_model().objects.create_superuser(
        email=superuser_email,
        password="DefaultPassword"
    )
    print("!!! superuser email for development environment: ", superuser_email, " !!!")
    groups_list = settings.GROUP_LIST
    for group in groups_list:
        GroupFactory.create(name=group)
    client_users = UserFactory.create_batch(100, assign_to_group="Client")
    support_users = UserFactory.create_batch(20, assign_to_group="Support")

    print(str(get_user_model().objects.all().count()), "users created. ")
