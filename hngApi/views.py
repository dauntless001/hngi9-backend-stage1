from django.http import JsonResponse

def index_view(request):
    return JsonResponse(
        {
            'slackUsername' : 'Oluwaseun Matanmi', 
            'backend' : True, 'age' : 20, 'bio' : 'A focused, talented young boy, who is optimistic on becoming the next sensation. I love python, Javascript & Virtual Reality'
        }
    )