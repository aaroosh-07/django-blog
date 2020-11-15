from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('post/<int:id>/', views.index , name = "index" ),
    path('update/<int:id>/', views.update , name = "update-post" ),
    path('', views.home , name = "home" ),
    path('create/', views.create , name = "create" ),
    path('profile/<str:username>/',views.profile , name = "profile"),
    path('edit/',views.edit,name="edit_user")
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)