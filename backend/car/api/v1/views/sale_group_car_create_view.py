from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from car.repositories import CarRepository
from car.api.v1.serializers import (
    SaleGroupCreateCarSerializer,
    SaleGroupDetailCarSerializer
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from core.permissions import IsAuthenticatedSeller

car_repository = CarRepository()


@api_view(["POST"])
@permission_classes([IsAuthenticatedSeller])
@authentication_classes([JWTAuthentication])
def sale_group_car_create_view(request):
    serializer = SaleGroupCreateCarSerializer(data=request.data)
    if not serializer.is_valid():
        response = {
            "status": "failed",
            "message": "car update failed.",
            "data": {"errors": serializer.errors}
        }
        return Response(
            response,
            status=status.HTTP_400_BAD_REQUEST
        )
    car = car_repository.create_car(
        title=serializer.validated_data.get('title'),
        description=serializer.validated_data.get('description'),
        color=serializer.validated_data.get('color'),
        carrying_capacity=serializer.validated_data.get('carrying_capacity'),
        cylinder_number=serializer.validated_data.get('cylinder_number'),
        cylinder_capacity=serializer.validated_data.get('cylinder_capacity'),
        owner_id=request.user.id
    )
    serializer = SaleGroupDetailCarSerializer(car)
    response = {
        "status": "success",
        "message": "car update successfully.",
        "data": serializer.data
    }
    return Response(response, status=status.HTTP_200_OK)


