from .models import Movie, Actor, Review
from .serializers import MovieSerializers, ActorSerializers, ReviewSerializers
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def actor_list(request):
    if request.method == 'GET':
        actors = Actor.objects.all()
        serializer = ActorSerializers(actors, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def actor_detail(request, pk):
    if request.method =='GET':
        actor = Actor.objects.get(pk=pk)
        movie = Movie.objects.get()
        serializer = ActorSerializers(actor)
        return Response(serializer.data)