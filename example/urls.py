from django.urls import path
from example import views

urlpatterns = [
    path("", views.index, name="index"),
    path("show_messages/", views.show_messages, name="show_messages"),
]

app_name = "example"
