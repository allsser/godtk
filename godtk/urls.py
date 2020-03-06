from django.urls import path
from . import views

app_name = 'godtk'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:godtk_pk>/', views.detail, name='detail'),
    path('<int:godtk_pk>/delete/', views.delete, name='delete'),
    path('<int:godtk_pk>/update/', views.update, name='update'),
    path('<int:hash_pk>/hashtag/', views.hashtag, name='hashtag'),
    path('search/', views.search, name='search'),
]