# from rest_framework.response import Response. To return a api response
from rest_framework.decorators import api_view
from django.http import JsonResponse # To return json

@api_view(['GET'])
def student (request):
    person = {
        'slackUsername': 'Olatomide',
        'backend': True,
        'age' : 30,
        'bio' : 'I am cool person that loves to meet people. My aim is to learn better'
    }
    #return Response(person)
    return JsonResponse(person)