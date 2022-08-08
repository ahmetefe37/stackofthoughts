from django.urls import path

from thought import views

urlpatterns = [
    path('', views.f_homepage,name="url_homepage"),
]