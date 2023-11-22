from rest_framework_simplejwt import exceptions
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.response import Response
from rest_framework import status


class CustomRefreshTokenView(TokenRefreshView):

    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            response.data = {
                "status": "success",
                "message": "token refreshed successfully.",
                "data": response.data
            }
            return response
        except exceptions.AuthenticationFailed:
            return Response(
                {
                    "status": "failed",
                    "message": "Invalid token.",
                },
                status=status.HTTP_401_UNAUTHORIZED
            )
