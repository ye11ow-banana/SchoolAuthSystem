from django.db.models import QuerySet
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView
from django.views.generic.detail import SingleObjectMixin

from workers.forms import WorkerListForm
from workers.models import WorkerList


class WorkerListsView(ListView):
    """
    View for Worker Lists page.
    """
    model = WorkerList
    paginate_by = 4
    context_object_name = 'worker_lists'
    template_name = 'workers/worker_lists.html'


class WorkerListView(UpdateView, SingleObjectMixin):
    """
    View for Worker List Detail page.
    Contains workers of Worker List.
    """
    model = WorkerList
    context_object_name = 'worker_list'
    template_name = 'workers/worker_list.html'
    form_class = WorkerListForm
    object = None

    def get_context_data(self, **kwargs) -> dict:
        self.object = self.get_object()
        return super().get_context_data(**kwargs)

    def get_success_url(self) -> str:
        return self.request.path

    def get_form_kwargs(self) -> dict:
        kwargs = super().get_form_kwargs()
        kwargs.update({'instance': self.object})
        return kwargs


class WorkerListsSearchView(WorkerListsView):
    """
    Search on Worker Lists page.
    """
    def get_queryset(self) -> QuerySet:
        return self.model.objects.filter(title__icontains=self.request.GET['q'])

    def get_context_data(self, *args, **kwargs) -> dict:
        context = super().get_context_data(*args, **kwargs)
        context['q'] = f'q={self.request.GET["q"]}&'
        return context


worker_lists_view = WorkerListsView.as_view()
worker_list_view = WorkerListView.as_view()
worker_lists_search_view = WorkerListsSearchView.as_view()
worker_list_delete_view = DeleteView.as_view(
    model=WorkerList,
    success_url=reverse_lazy('workers:worker_lists')
)
