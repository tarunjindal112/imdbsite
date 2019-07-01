from .models import Movie
from .serializers import MovieSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class IndexView(APIView):
    """
    API view for searching Movies
    """
    allowed_methods = ['GET']
    serializer_class = MovieSerializer

    def get(self, request, *args, **kwargs):
        queryset = Movie.objects.all()

        # We can filter our movies by name
        name = request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)

        # We can filter our movies by director
        director = request.query_params.get('director', None)
        if director is not None:
            queryset = queryset.filter(director__icontains=director)

        # We can filter our movies by genre
        genre = request.query_params.get('genre', None)
        if genre is not None:
            queryset = queryset.filter(genre__name__icontains=genre)

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
