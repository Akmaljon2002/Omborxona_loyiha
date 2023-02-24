from django.contrib import admin
from django.urls import path
from asosiy.views import *
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', StatsView.as_view()),
    path('stats_del/<int:pk>/', StatsDeleteView.as_view(), name="stat-del"),
    path('stats_edit/<int:pk>/', StatsEditView.as_view(), name="stats-edit"),
]
