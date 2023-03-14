from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),

    path('novo/', views.newContact, name='novo'),

    path('detalhes/<str:pk>/', views.detailsContact, name="detalhes"),
    path('editar/<str:pk>/', views.editContact, name="editar"), 
    path('apagar/<str:pk>/', views.deleteContact,name="apagar")


]