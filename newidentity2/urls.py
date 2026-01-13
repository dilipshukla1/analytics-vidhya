from django.contrib import admin
from django.urls import path
from identity.views import login_view, profile_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/login/', login_view),
    path('api/user-rest-galaxy/profile/', profile_view),
]

