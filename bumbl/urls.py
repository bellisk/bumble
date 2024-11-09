from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path('__page/(?P<from_index>[0-9]+)/(?P<path>.*)', views.page, name="page"),
    re_path(r'^(?P<path>.*)$', views.entry, name="entry")
]
