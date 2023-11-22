from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from core.services import RegisterUserService
from core.api.v1.serializers import RegisterClientUserSerializer
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes
)


user_service = RegisterUserService()


@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def register_client_user_view(request):
    serializer = RegisterClientUserSerializer(data=request.data)
    if not serializer.is_valid():
        response = {
            "status": "failed",
            "message": "client registration failed.",
            "data": {"errors": serializer.errors}
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    # we can return some config data for caching,
    # this practice can prevent extra requests
    user = user_service.register_client_user(
        first_name=serializer.validated_data.get("first_name"),
        last_name=serializer.validated_data.get("last_name"),
        email=serializer.validated_data.get("email"),
        password=serializer.validated_data.get("password"),
        fcm_token=serializer.validated_data.get("fcm_token")
    )
    refresh = RefreshToken.for_user(user)
    response = {
        "status": "success",
        "message": "client registered successfully.",
        "data": {
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }
    }
    return Response(response, status=status.HTTP_201_CREATED)
