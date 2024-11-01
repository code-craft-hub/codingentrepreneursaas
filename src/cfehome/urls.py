from django.contrib import admin
from django.urls import path
from .view import home_page_view,my_home_page_view

urlpatterns = [
    path("", my_home_page_view),
    path('admin/', admin.site.urls),
    path("hello-world.codecrafthub", home_page_view)
]
