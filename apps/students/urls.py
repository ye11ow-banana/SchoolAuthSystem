from django.urls import path, include

from . import views

app_name = 'students'

subject_urlpatterns = [
    path('create/', views.subject_create_view, name='subject_create'),
    path('list/', views.subject_list_view, name='subject_list'),
    path('detail/<int:pk>/', views.subject_detail_view, name='subject_detail'),
    path('<int:pk>/update/', views.subject_update_view, name='subject_update'),
    path('<int:pk>/delete/', views.subject_delete_view, name='subject_delete')
]

urlpatterns = [
    path('subject/', include(subject_urlpatterns))
]
