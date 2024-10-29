from django.urls import path

from . import views

urlpatterns = [
    path(r'__page/([0-9]+)/<path>', views.page, name="page"),
    path(r'<path>', views.entry, name="entry")
]
