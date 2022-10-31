from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class IndexView(APIView):
    def get(self, request, format=None):
        data = {
            'slackUsername' : 'omatanmi', 
            'backend' : True, 'age' : 20, 'bio' : 'A focused, talented young boy, who is optimistic on becoming the next sensation. I love python, Javascript & Virtual Reality'
        }
        return Response(data, status=status.HTTP_200_OK)