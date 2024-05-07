from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListView, GenreDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', GenreCreateListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>', GenreDetailView.as_view(), name='genre-detail'),
]
