from django.urls import path
from . import views


urlpatterns = [
    path(
        'genres/',
        views.GenreCreateListView.as_view(),
        name='genre-criate-list'
    ),
    path(
        'genres/<int:pk>',
        views.GenreRetriveUpdateDestroyView.as_view(),
        name='gente-detail-view'
    ),
]
