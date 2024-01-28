from django.contrib import admin
from django.urls import path

from sitevs.views import(
SitevListView, 
SitevCreateView, 
SitevUpdateView, 
SitevDeleteView,
SitevCompleteView,
) 
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", SitevListView.as_view(), name="sitev_list"),
    path("create", SitevCreateView.as_view(), name="sitev_create"),
    path("update/<int:pk>", SitevUpdateView.as_view(), name="sitev_update"),
    path("delete/<int:pk>", SitevDeleteView.as_view(), name="sitev_delete"),
    path("complete/<int:pk>", SitevCompleteView.as_view(), name="sitev_complete"),
]
