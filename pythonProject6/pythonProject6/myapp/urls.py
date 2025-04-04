from django.urls import path
from . import views
from .views import CustomLoginView, register, user_logout

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('register/', register, name="register"),
    path('logout/', user_logout, name='logout'),
]