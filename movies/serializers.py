
from dataclasses import fields
from rest_framework import serializers
from .models import Actor, Movie, Review

class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class MovietitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title',)


class ActorSerializer(serializers.ModelSerializer):
    movies = MovietitleSerializer(many=True)
    class Meta:
        model = Actor
        fields = ['id', 'name', 'movies']


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'overview',)
        
class MovieSerializer(serializers.ModelSerializer):
    class AcotrNameSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name',)
    

    class MovieReviewsSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('title', 'content',)

    actors = AcotrNameSerializer(many=True)
    review_set = MovieReviewsSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'content',)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ReviewDetailSerializer(serializers.ModelSerializer):
    class MovieTitleNameSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)

    movie = MovieTitleNameSerializer()
    class Meta:
        model = Review
        fields = '__all__'

class ReviewCreateSerializer(serializers.ModelSerializer):
    class MovieInfoSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)
    movie = MovieInfoSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ('id', 'movie', 'title', 'content',)
