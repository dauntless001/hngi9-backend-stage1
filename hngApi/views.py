from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from hngApi.api.serializers import ArithmeticSerializer
import re, enum



headers = {
    'accept' : '*',
    'Content-Type' : 'application/json',
    'Access-Control-Allow-Origin' : '*',
}


class IndexView(APIView):
    def get(self, request, format=None):
        data = {
            'slackUsername' : 'omatanmi', 
            'backend' : True, 'age' : 20, 'bio' : 'A focused, talented young boy, who is optimistic on becoming the next sensation. I love python, Javascript & Virtual Reality'
        }
        
        return Response(data, status=status.HTTP_200_OK, headers=headers)

class Operator(enum.Enum):
    addition = 'addition'
    subtraction = 'subtraction'
    multiplication = 'multiplication'


class ArithmeticView(APIView):
    serializer_class = ArithmeticSerializer



    def post(self, request, format=None):
        json = request.POST
        result = 0
        x = request.POST['x']
        y = request.POST['y']
        operator = None
        operation_type = request.POST['operation_type']
        if operation_type == Operator.addition.name:
            result = int(x) + int(y)
            operator = Operator.addition
        elif operation_type == Operator.subtraction.name:
            result = int(x) - int(y)
            operator = Operator.subtraction
        elif operation_type == Operator.multiplication.name:
            result = int(x) * int(y)
            operator = Operator.multiplication
        data = {
            'slackUsername':'omatanmi',
            'operation_type' : operator.value,
            'result' : result
        }
        return Response(data, status=status.HTTP_200_OK, headers=headers)
