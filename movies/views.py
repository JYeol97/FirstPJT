from .models import Movie, Actor, Review
from .serializers import MovieSerializers, ActorSerializers, ReviewSerializers, ActorDetailSerializers, MovieDetailSerializers
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
        serializer = ActorDetailSerializers(actor)
        return Response(serializer.data)
    

@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        serializer = MovieSerializers(movie, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, pk):
    if request.method == 'GET':
        movie = Movie.objects.get(pk=pk)
        serializer = MovieDetailSerializers(movie)
        return Response(serializer.data)

@api_view(['GET'])
def review_list(request):
    if request.method == 'GET':
        review = Review.objects.all()
        serializer = ReviewSerializers(review, many=True)
        return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def review_detail(request,pk):
    if request.method == 'GET':
        review = Review.objects.get(pk=pk)
        serializer = ReviewSerializers(review, many=True)
        return Response(serializer.data)
        
    if request.method == 'PUT':
        
        pass
    if request.method == 'DLETE':
        pass

@api_view(['POST'])
def create_review(request):
    if request.method == 'POST':
        pass
    