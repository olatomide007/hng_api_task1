from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def student (request):
    person = {
        'slackUsername': 'Olatomide',
        'backend' : 'True',
        'age' : '30',
        'Bio' : 'I am cool person that loves to meet people. My aim is to learn better'
    }
    return Response(person)