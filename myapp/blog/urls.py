from django.urls import path
from . import views

app_name = "blog"

urlpatterns=[
    path("", views.index, name="index"),
    path("detail/<str:slug>",views.detail, name="detail"),
    path("contact",views.contact,name="contact"),
    path("about",views.about_us,name="about")
]
