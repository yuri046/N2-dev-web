from django.urls import path

from . import views

app_name = 'categories'

urlpatterns = [
    path('', views.list_categories, name='list_categories'),
    path('adicionar/', views.add_category, name='add_category'),
    path('editar/<int:id_category>/', views.edit_category, name='edit_category'),
    path('excluir/<int:id_category>/', views.delete_category, name='delete_category'),
]