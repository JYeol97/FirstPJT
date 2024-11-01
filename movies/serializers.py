from dataclasses import field
from .models import Movie,Actor,Review
from rest_framework import serializers

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title','overview')

class ActorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ReviewDetailSerializers(serializers.ModelSerializer):
    class ReviewMovieSerializers(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)
    movie = ReviewMovieSerializers()
    class Meta:
        model = Review
        fields = '__all__'



# 아래 두개는 디테일과 관련된 직렬화
# ActorMoviesSerializers는 영화중 title만 가져오고 
# ActorDetailSerializers는 title중 actors_movies(역참조)에 해당하는 것만
# 추려서 넣어줌
class ActorMoviesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title',)

class ActorDetailSerializers(serializers.ModelSerializer):
    movies = ActorMoviesSerializers(many = True, read_only=True)
    class Meta:
        model = Actor
        fields = ('id','name','movies')

class MovieDetailSerializers(serializers.ModelSerializer):
    class ActorNameSerializers(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name',)
    
    class MovieReviewsSerializers(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = '__all__'
    actors = ActorNameSerializers(many = True)
    review_set = MovieReviewsSerializers(many=True)
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewCreateSerializers(serializers.ModelSerializer):
    class ReviewMovieSerializers(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)
    movie = ReviewMovieSerializers(read_only=True)
    class Meta:
        model = Review
        fields = ('id','movie',"title","content")

'''
ㅋㅋ
'''