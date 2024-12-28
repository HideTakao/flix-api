from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListView,GenreRetriveUpdateDestroyView
from actors.views import ActorCreatListView, ActorRetriveUpdateDestroyView
from movies.views import MovieCreateListView, MovieRetrieveUpdateDestroyView
from reviews.views import ReviewCreateListView, ReviewRetrieveUpdateDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres', GenreCreateListView.as_view(), name='genre-criate-list'),
    path('genres/<int:pk>', GenreRetriveUpdateDestroyView.as_view(), name='gente-detail-view'),

    path('actors', ActorCreatListView.as_view(), name='actor-criate-list'),
    path('actors/<int:pk>', ActorRetriveUpdateDestroyView.as_view(), name='actor-detail-view'),

    path('movies', MovieCreateListView.as_view(), name='movie-criate-list'),
    path('movies/<int:pk>', MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail-view'),

    path('reviews', ReviewCreateListView.as_view(), name='reviews-create-view'),
    path('reviews/<int:pk>', ReviewRetrieveUpdateDestroyView.as_view(), name='reviews-detail-view'),
]