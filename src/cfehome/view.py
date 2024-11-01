from django.http import HttpResponse
import pathlib
from django.shortcuts import render
from visits.models import PageVisit
this_dir = pathlib.Path(__file__).resolve().parent


def home_page_view(request, *args, **kwargs):
    # queryset = PageVisit.objects.all()
    queryset = PageVisit.objects.filter(path=request.path)
    PageVisit.objects.create(path=request.path)

    return render(request, "home.html", {
        "page_title": "From View.py",
        "queryset": queryset.count()
    })

def my_home_page_view(request, *args, **kwargs):
    return HttpResponse("<h1> This is the Home Page. </h1>")