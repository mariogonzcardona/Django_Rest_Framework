from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user.api.views import RegisterView,UserView

urlpatterns = [
    path('auth/register',RegisterView.as_view(),name='register'),
    path('auth/login',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('auth/token/refresh',TokenRefreshView.as_view(),name='token_refresh'),
    path('auth/me',UserView.as_view(),name='user_me'),
]