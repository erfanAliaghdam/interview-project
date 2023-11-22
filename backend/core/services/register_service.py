import logging
from django.db import transaction
from core.exceptions import Custom500Exception
from users.repositories import UserRepository


class RegisterUserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def register_client_user(
            self,
            first_name: str,
            last_name: str,
            email: str,
            password: str,
            fcm_token: str
    ):
        try:
            with transaction.atomic():
                # why transaction atomic: verification email
                # on user registration is very important
                # atomic can prevent user bad experiences on registration
                user = self.user_repository.register_client_user(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password,
                    fcm_token=fcm_token
                )
                # TODO: send email
                return user
        except Exception as e:
            logging.error(f"Failed on register client user. {e}")
            raise Custom500Exception("something went wrong. please try again later.")
