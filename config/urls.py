from django.contrib import admin
from django.urls import path
from game import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("main/", views.main),
    path("gameing/",views.gameing),
    #path("over_win/", admin.over_win),
    #path("over_lose/", admin.over_lose),
    ]
