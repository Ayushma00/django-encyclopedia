from django.urls import path

from . import views
app_name="encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>",views.index1,name="index1"),
    path("search",views.search,name="search"),
    path("mywords",views.mywords,name="mywords"),
    path("/random",views.random,name="random"),
    path("edit/<str:name>",views.edit,name="edit")
]
