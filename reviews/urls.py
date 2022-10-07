from django.urls import URLPattern, path
from . import views

app_name = "reviews"

urlpatterns = [
    path("reviews/", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:pk>/", views.detail, name="detail"),
]
