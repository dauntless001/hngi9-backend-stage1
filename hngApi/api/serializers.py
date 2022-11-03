from rest_framework import serializers


class ArithmeticSerializer(serializers.Serializer):
    x = serializers.IntegerField()
    y = serializers.IntegerField()
    operation_type = serializers.CharField()