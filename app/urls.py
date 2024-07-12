from django.contrib import admin
from django.urls import path, include, re_path
# from django.urls import path, include


# from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('audit/', include('audit.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('report_builder/', include('report_builder.urls')),
]

