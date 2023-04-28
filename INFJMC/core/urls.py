from django.urls import path

from . import views

urlpatterns = [
    path("core/", views.home, name="home"),
    path("core/carreras", views.carreras, name="carreras"),
    path("core/docentes", views.docentes, name="docentes")
]