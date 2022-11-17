from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.views import LoginView

urlpatterns = [
    path("", include("core.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(redirect_authenticated_user=True), name="login"),
    path('admin/', admin.site.urls),
]
