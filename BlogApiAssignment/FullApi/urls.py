from django.urls import path
from .views import getRoutes, BlogAPI, RegisterAPI, GetUserAPI
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("", getRoutes, name="Routes"),
    path("blog", BlogAPI.as_view(), name="Blog"),
    path("register", RegisterAPI.as_view(), name="Register"),
    path("login", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("userdetial", GetUserAPI.as_view(), name="user_detial"),
    # path("books/<int:id>", BooksAPI.as_view(), name="Books"),
    # path("savebooks", saveBooks, name="SaveBooks"),
]
 