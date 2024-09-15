from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('token/refresh/', TokenRefreshView.as_view(),name='token_refresh'),
    path('token/', TokenObtainPairView.as_view(),name='token_obtain_pair'),
]

