"""
This file contains the views for the API.
"""
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics


class HealthCheckView(generics.GenericAPIView):
    """
    This view is used to check the health of the server.
    """
    def get(self, request):
        """
        This method is used to check the health of the server.
        :param request:
        :return:
        """
        # Here, you can add any application health check logic you need.
        # For the sake of simplicity, this endpoint will always return that the server is running fine.
        return Response({"status": "Server is running fine"}, status=status.HTTP_200_OK)
