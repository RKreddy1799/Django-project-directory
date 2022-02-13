from django.http import JsonResponse

def hello(request):

    data = {'Message': 'Hello World!'}

    return JsonResponse(data, safe=False)