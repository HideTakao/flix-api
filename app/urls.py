from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListView,GenreRetriveUpdateDestroyView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres', GenreCreateListView.as_view(), name='genre'),
    path('genres/<int:pk>', GenreRetriveUpdateDestroyView.as_view(), name='gente-detail-view'),
]