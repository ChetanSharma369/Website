from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializer import PersonSerializer

# Create your views here.
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def index(request):
    cources = {
        'course_name': 'python',
        'learn': ['django','flask', 'tornado'],
        'provider':'chetan'
    }
    if request.method == 'GET':
        cources['method'] = 'YOU hit GET'
        return Response(cources)
    elif request.method == 'POST':
        cources['method']= 'you hit POST method' 
        return Response(cources)
    else:
        return Response(cources)
    
@api_view(['GET','POST','PUT','PATCH'])
def person(request):
    if request.method == 'GET':
        data = Person.objects.all()
        serializer = PersonSerializer(data, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PUT':
        data = request.data
        model_id = Person.objects.get(id=data.get('id'))
        seralize = PersonSerializer(model_id, data=data)
        if seralize.is_valid():
            seralize.save()
            return Response(seralize.data)
        return Response(seralize.errors)
    elif request.method == 'PATCH':
        data = request.data
        model_id = Person.objects.get(id=data.get('id'))
        seralize = PersonSerializer(model_id, data=data, partial=True)
        if seralize.is_valid():
            seralize.save()
            return Response(seralize.data)
        return Response(seralize.errors)
    
def person_delete(request,id):
    model_id = Person.objects.get(id=id)
    model_id.delete()
    return Response({'message': "Deleted sucessfully"})