from django.contrib import admin
from django.urls import path,include
from .views import drink_list
from . import views
urlpatterns = [
    path("drink-list/",views.drink_list),
    path("drink-list/<int:id>",views.drink_detail)
    ]
