from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from car.api.v1.serializers import SupportCarListSerializer
from car.repositories import CarRepository
from core.permissions import IsAuthenticatedSupport
from rest_framework_simplejwt.authentication import JWTAuthentication


car_repository = CarRepository()


@api_view(["GET"])
@permission_classes([IsAuthenticatedSupport])
@authentication_classes([JWTAuthentication])
def support_group_car_list_view(request):
    paginator = PageNumberPagination()
    paginator.page_size = 5
    cars = car_repository.get_all_cars_and_owner_details()
    paginated_cars = paginator.paginate_queryset(cars, request)

    serializer = SupportCarListSerializer(paginated_cars, many=True)

    response = {
        "status": "success",
        "message": "car list retrieved successfully.",
        "data": serializer.data,
        "pagination": {
            "next": paginator.get_next_link(),
            "previous": paginator.get_previous_link(),
            "count": paginator.page.paginator.count,
        }
    }

    return Response(
        response,
        status=status.HTTP_200_OK
    )
