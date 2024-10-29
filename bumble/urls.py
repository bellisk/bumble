from django.urls import path

from . import views

urlpatterns = [
    path(r'__page/([0-9]+)/(.*)', views.page, name="page"),
    path(r'(.*)', views.entry, name="entry")
]
