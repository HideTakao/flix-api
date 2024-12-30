from django.urls import path
from . import views

urlpatterns = [
    path(
        'actors/',
        views.ActorCreatListView.as_view(),
        name='actor-criate-list'
    ),
    path(
        'actors/<int:pk>',
        views.ActorRetriveUpdateDestroyView.as_view(),
        name='actor-detail-view'
    ),
]