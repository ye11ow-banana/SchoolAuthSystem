from django.urls import path

from . import views

app_name = 'workers'

urlpatterns = [
    path('worker_lists/', views.worker_lists_view, name='worker_lists'),
    path('worker_list/<int:pk>/', views.worker_list_view, name='worker_list'),
    path('worker_lists/search', views.worker_lists_search_view, name='worker_lists_search')
]
