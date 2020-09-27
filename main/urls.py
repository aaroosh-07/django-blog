from django.urls import path
from . import views

urlpatterns = [
    path('post/<int:id>/', views.index , name = "index" ),
    path('update/<int:id>/', views.update , name = "update-post" ),
    path('', views.home , name = "home" ),
    path('create/', views.create , name = "create" ),
    path('profile/<str:username>/',views.profile , name = "profile")
]