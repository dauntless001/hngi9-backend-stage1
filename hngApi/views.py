from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from hngApi.api.serializers import ArithmeticSerializer
import re



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

class ArithmeticView(APIView):
    serializer_class = ArithmeticSerializer

    def get_operations(self, operand):
        operation = {
            'addition' : 'addition',
            'subtraction' : 'subtraction',
            'multiplication' : 'multiplication'
        }
        return operation[operand]



    def post(self, request, format=None):
        json = request.POST
        x = request.POST['x']
        y = request.POST['y']
        operation_type = request.POST['operation_type']
        if operation_type == 'addition':
            result = int(x) + int(y)
        elif operation_type == 'subtraction':
            result = int(x) - int(y)
        elif operation_type == 'multiplication':
            result = int(x) * int(y)
            operation_type = 'multiplication'
        data = {
            'slackUsername':'omatanmi',
            'operation_type' : self.get_operations(operation_type),
            'result' : result
        }
        return Response(data, status=status.HTTP_200_OK, headers=headers)
