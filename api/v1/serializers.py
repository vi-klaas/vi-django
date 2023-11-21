"""
Serializers for the API
"""
from rest_framework import serializers


class HealthCheckSerializer(serializers.Serializer):
    """
    Serializer for the health check endpoint.
    """
    def create(self, validated_data):
        """

        :param validated_data:
        :return:
        """
        pass

    def update(self, instance, validated_data):
        """

        :param instance:
        :param validated_data:
        :return:
        """
        pass
