# python system modules
from django.urls import path

# my modules
from thought import views

# --------------------------------------------------------------------
urlpatterns = [
    path('', views.f_homepage,name="url_homepage"),

    path('detail/',views.f_detailpage,name="url_detailpage"),

    path('contact/', views.f_contactpage, name="url_contactpage"),
    path('aboutus/', views.f_aboutuspage, name="url_aboutuspage"),

    path('register/', views.f_registerpage, name="url_registerpage"),
    path('login/', views.f_loginpage, name="url_loginpage"),
    path('profile/', views.f_profilepage, name="url_profilepage"),

]