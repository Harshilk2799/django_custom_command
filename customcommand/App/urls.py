from django.urls import path
from App import views

urlpatterns = [
    path("", views.index, name="index"),
    path("print_message/", views.print_message, name="print_message"),
]
