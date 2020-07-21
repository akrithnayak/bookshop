from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="store-home"),
    path("admin/", views.admin, name="store-admin"),
    path("admin/home", views.adminHome, name="admin-home"),
    path("admin/home/search", views.adminSearch, name="admin-home-search"),
    path("admin/home/save", views.adminSave, name="admin-home-save"),
    path("admin/home/add", views.adminAdd, name="admin-home-add"),
    path("admin/home/delete", views.adminDelete, name="admin-home-delete"),
    path("about/", views.about, name="store-about"),
    path("result/", views.result, name="store-search"),
    path("auth/", views.adminAuth, name="admin-auth")
]