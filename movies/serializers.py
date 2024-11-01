from rest_framework import serializers
from .models import Actor, Movie, Review

class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    movies = serializers.StringRelatedField(many=True)
    class Meta:
        model = Actor
        fields = ['id', 'name', 'movies']

class MovietitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Movie
        
class MovieDetailSerializer(serializers.ModelSerializer):
    class AcotrNameSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name',)
    
    class MovieReviewsSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = '__all__'

    actors = AcotrNameSerializer(many=True)
    reviews = MovieReviewsSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'

