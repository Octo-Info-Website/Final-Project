from django.urls import path
from . import views

urlpatterns = [
    path("facts", views.facts, name = "facts"),
    path("member/<int:member_id>", views.UserPage, name = "UserPage"),
    path("", views.index, name = "index"),
    
]