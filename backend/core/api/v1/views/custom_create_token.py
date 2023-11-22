from rest_framework_simplejwt import exceptions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status


class CustomTokenObtainPairView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            response.data = {
                "status": "success",
                "message": "token created successfully.",
                "data": response.data
            }
            return response
        except Exception as e:
            return Response(
                {
                    "status": "failed",
                    "message": "Invalid Username or Password.",
                },
                status=status.HTTP_401_UNAUTHORIZED
            )
