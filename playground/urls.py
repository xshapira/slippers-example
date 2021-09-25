from django.urls import path
from playground.views import index

urlpatterns = [
    path("", index)
]
