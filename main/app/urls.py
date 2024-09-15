from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<str:model_name>/<int:pk>', views.detail, name='detail'),
    path('blog', views.comment, name='comment'),
    path('comment/update/<int:pk>', views.update_comment, name='update_comment'),
]