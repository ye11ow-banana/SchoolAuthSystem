from django.urls import path

from . import views

app_name = 'workers'

urlpatterns = [
    path('worker_lists/', views.worker_lists_view, name='worker_lists'),
    path('worker_lists/search', views.worker_lists_search_view, name='worker_lists_search'),
    path('worker_list/<int:pk>/', views.worker_list_view, name='worker_list'),
    path('worker_list/<int:pk>/delete/', views.worker_list_delete_view, name='worker_list_delete'),
    path('worker_list/<int:pk>/update/', views.worker_list_update_view, name='worker_list_update'),
    path('worker_list/create/', views.worker_list_create_view, name='worker_list_create'),
    path('worker_list/<int:pk>/search/', views.workers_search_view, name='workers_search'),
    path('worker_list/<int:pk>/filter/', views.workers_filter_view, name='workers_filter')
]
