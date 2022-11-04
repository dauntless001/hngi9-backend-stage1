from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from hngApi.api.funcs import ADDITION, MULTIPLICATION, SUBTRACTION, translate_text
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

    def process_command(self, operation_type, x, y):
        if operation_type in ADDITION:
            result = int(x) + int(y)
            operator = Operator.addition
        elif operation_type in SUBTRACTION:
            result = int(x) - int(y)
            operator = Operator.subtraction
        elif operation_type in MULTIPLICATION:
            result = int(x) * int(y)
            operator = Operator.multiplication
        return {'result':result, 'operator':operator}


    def post(self, request, format=None):
        x = request.POST.get('x', '')
        y = request.POST.get('y', '')
        operation_type = request.POST.get('operation_type', '')
        data = {
            'slackUsername':'omatanmi',
            'operation_type' : None,
            'result' : 0
        }
        if len(operation_type.split()) > 1:
            ops = translate_text(operation_type)
            solution = self.process_command(ops['operation_type'], ops['x'], ops['y'])
            data['result'] = solution['result']
            data['operation_type'] = solution['operator'].value
        else:
            solution = self.process_command(operation_type, x, y)
            data['result'] = solution['result']
            data['operation_type'] = solution['operator'].value
        return Response(data, headers=headers)
