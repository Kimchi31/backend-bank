from rest_framework import routers
from django.urls import path, include
from .views import index, ReportViewSet,report
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'reports', ReportViewSet, basename='reports')

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('index/', index, name='index'),
    path('create-reports/', report, name='report'),
    path('login/', views.login_view, name='custom_login'),
    path('api/', include(router.urls)),
]
