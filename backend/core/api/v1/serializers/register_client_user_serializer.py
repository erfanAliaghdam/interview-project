from rest_framework import serializers
from users.repositories import UserRepository


class RegisterClientUserSerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_repository = UserRepository()

    first_name = serializers.CharField(
        required=True,
        max_length=255,
        error_messages={
            "invalid": "first name is invalid.",
            "required": "first name is required.",
            "blank": "first name is invalid.",
            "null": "first name is invalid.",
        }
    )
    last_name = serializers.CharField(
        required=True,
        max_length=255,
        error_messages={
            "invalid": "last name is invalid.",
            "required": "last name is required.",
            "blank": "last name is invalid.",
            "null": "last name is invalid.",
        }
    )
    email = serializers.EmailField(
        required=True,
        max_length=255,
        error_messages={
            "invalid": "email is invalid.",
            "required": "email is required.",
            "blank": "email is invalid.",
            "null": "email is invalid.",
        }
    )
    password = serializers.CharField(
        required=True,
        max_length=255,
        error_messages={
            "invalid": "password is invalid.",
            "required": "password is required.",
            "blank": "password is invalid.",
            "null": "password is invalid.",
        }
    )
    fcm_token = serializers.CharField(
        required=True,
        max_length=255,
        error_messages={
            'invalid': "fcm token is invalid.",
            'required': "fcm token is required.",
            "blank": "fcm token is invalid.",
            "null": "fcm token is invalid.",
        }
    )

    def validate_email(self, email):
        if self.user_repository.check_if_client_user_exists(email=email):
            raise serializers.ValidationError("user with this email exists.")
        return email
