from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.booklist_form, name='booklist_insert'),
    path('<int:id>/', views.booklist_form, name='booklist_update'),
    path('delete/<int:id>/',views.booklist_delete,name='booklist_delete'),
    path('list/', views.booklist_list,name='booklist_list')
]