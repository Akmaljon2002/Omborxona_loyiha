from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', BolimlarView.as_view()),
    path('mahsulotlar/', MahsulotlarView.as_view(), name="mahsulotlar"),
    path('clientlar/', ClientlarView.as_view(), name="clients"),
    path('mahsulot_del/<int:pk>/', MahsulotDeleteView.as_view(), name="mahsulot-del"),
    path('mahsulot_edit/<int:pk>/', MahsulotEditView.as_view(), name="mahsulot-edit"),
]
