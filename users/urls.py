from django.urls import path 
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenBlacklistView,
)
from . import views

urlpatterns = [
    path('signup/', views.UserView.as_view(), name='user_view'),
    path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('<int:user_id>/', views.UserProfileView.as_view(), name="profile_view"),
]