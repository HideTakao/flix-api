from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListView,GenreRetriveUpdateDestroyView
from actors.views import ActorCreatListView, ActorRetriveUpdateDestroyView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres', GenreCreateListView.as_view(), name='genre-criate-list'),
    path('genres/<int:pk>', GenreRetriveUpdateDestroyView.as_view(), name='gente-detail-view'),
    path('actors', ActorCreatListView.as_view(), name='actor-criate-list'),
    path('actors/<int:pk>', ActorRetriveUpdateDestroyView.as_view(), name='actor-detail-view'),
]