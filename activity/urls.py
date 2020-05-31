from django.urls import path

version=1
from .views import *

views = [
        DetailListView,
]
urlpatterns = []
[urlpatterns.extend(view.urlpatterns(version)) for view in views]
