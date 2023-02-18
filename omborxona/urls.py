from django.contrib import admin
from django.urls import path, include
from asosiy.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bolim/', include('asosiy.urls')),
    path('stats/', include('statsapp.urls')),
    path('', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
]
