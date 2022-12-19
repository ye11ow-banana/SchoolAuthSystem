from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, ListView, DetailView,
    UpdateView, DeleteView
)

from .forms import SubjectForm
from .models import Subject


class SubjectCreateView(CreateView):
    model = Subject
    template_name = 'students/subject_creation.html'
    form_class = SubjectForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update(creator=self.request.user)
        return kwargs


subject_create_view = SubjectCreateView.as_view()
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
    template_name='students/subject_update.html',
    fields=('title',),
)
subject_delete_view = DeleteView.as_view(
    model=Subject,
    success_url=reverse_lazy('students:subject_list')
)
