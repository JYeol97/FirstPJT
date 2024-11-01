from .models import Movie, Actor, Review
from .serializers import ReviewDetailSerializers, ReviewCreateSerializers, MovieSerializers, ActorSerializers, ReviewSerializers, ActorDetailSerializers, MovieDetailSerializers
from rest_framework import serializers, status
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
    review = Review.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = ReviewSerializers(review)
        return Response(serializer.data)
        
    if request.method == 'PUT':
        serializer = ReviewDetailSerializers(review, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        review.delete()
        context = {
         'message': f'review {pk} is deleted.'   
        }
        return Response(context, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create_review(request,pk):
    if request.method == 'POST':
        movie = Movie.objects.get(pk=pk)
        serializer = ReviewCreateSerializers(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)