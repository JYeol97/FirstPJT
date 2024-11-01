from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MovieDetailSerializer, MovieSerializer, ActorListSerializer, ActorSerializer
from .models import Movie, Actor, Review
from movies import serializers

# Create your views here.
@api_view(['GET'])
def actor_list(request):
    actors = Actor.objects.all()
    serializer = ActorListSerializer(actors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def actor_detail(request, actor_pk):
    pass

@api_view(['GET'])
def movie_list(request):
    pass

@api_view(['GET'])
def movie_detail(request, movie_pk):
    pass

@api_view(['GET'])
def review_list(request):
    pass

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_pk):
    pass

@api_view(['POST'])
def create_review(request):
    pass