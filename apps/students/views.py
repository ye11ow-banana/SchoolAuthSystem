from django.views.generic import (
    CreateView, ListView, DetailView,
    UpdateView, DeleteView
)

from .models import Subject


subject_create_view = CreateView.as_view(
    model=Subject,
    template_name='students/subject_creation.html'
)
subject_list_view = ListView.as_view(
    model=Subject,
    context_object_name='subjects',
    template_name='students/subject_list.html'
)
subject_detail_view = DetailView.as_view(
    model=Subject,
    context_object_name='subject',
    template_name='students/subject_detail.html'
)
subject_update_view = UpdateView.as_view(
    model=Subject,
    template_name='students/subject_update.html'
)
subject_delete_view = DeleteView.as_view(model=Subject)
