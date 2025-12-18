from django.urls import path, include

from django.contrib import admin
from dj_rest_auth.views import LoginView, LogoutView
from dj_rest_auth.registration.views import RegisterView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/login/', LoginView.as_view(), name="login"),
    path('api/auth/logout/', LogoutView.as_view(), name="logout"),
    path('api/auth/register/', RegisterView.as_view(), name="register"),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/tasks/', include('task_api.urls')),

    # For Browseable API provided by 'rest_framework' Library
    # path('browser/', include('rest_framework.urls')),

]
