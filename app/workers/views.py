from django.db.models import QuerySet
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, DetailView

from workers.forms import WorkerListForm
from workers.models import WorkerList, Worker


class WorkerListsView(ListView):
    """
    View for Worker Lists page.
    """
    model = WorkerList
    paginate_by = 4
    context_object_name = 'worker_lists'
    template_name = 'workers/worker_lists.html'


class WorkerListView(DetailView):
    """
    View for Worker List Detail page.
    Contains workers of Worker List.
    """
    model = WorkerList
    context_object_name = 'worker_list'
    template_name = 'workers/worker_list.html'
    form_class = WorkerListForm

    def get_context_data(self, **kwargs) -> dict:
        worker_list = self.get_object()
        kwargs['workers'] = worker_list.worker_set.all()
        kwargs['form'] = self.form_class(instance=worker_list)
        return super().get_context_data(**kwargs)


class WorkerListsSearchView(WorkerListsView):
    """
    Search on Worker Lists page.
    """
    def get_queryset(self) -> QuerySet:
        return self.model.objects.filter(title__icontains=self.request.GET['q'])

    def get_context_data(self, **kwargs) -> dict:
        kwargs['q'] = f'q={self.request.GET["q"]}&'
        return super().get_context_data(**kwargs)


class WorkerListUpdateView(UpdateView, WorkerListView):
    """
    Updating `WorkerList` model on Worker List Detail page.
    """
    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        return context | dict(form=self.get_form())

    def get_success_url(self) -> str:
        return self.get_object().get_absolute_url()


worker_lists_view = WorkerListsView.as_view()
worker_list_view = WorkerListView.as_view()
worker_lists_search_view = WorkerListsSearchView.as_view()
worker_list_delete_view = DeleteView.as_view(
    model=WorkerList,
    success_url=reverse_lazy('workers:worker_lists')
)
worker_list_update_view = WorkerListUpdateView.as_view()
