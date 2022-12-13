from django.db.models import QuerySet
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DeleteView, UpdateView,
    DetailView, CreateView
)

from workers.forms import WorkerListForm
from workers.models import WorkerList
from workers.services import SearchService


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
    object = None

    def _get_workers_queryset(self) -> QuerySet:
        return self.object.workers.all()

    def get_context_data(self, **kwargs) -> dict:
        self.object = self.get_object()
        kwargs['workers'] = self._get_workers_queryset()
        kwargs['form'] = self.form_class(instance=self.object)
        return super().get_context_data(**kwargs)


class WorkerListsSearchView(WorkerListsView):
    """
    Search on Worker Lists page.
    """
    def get_queryset(self) -> QuerySet:
        search_service = SearchService(WorkerList.objects)
        return search_service.search_by_title(self.request.GET['q'])

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


class WorkerListCreateView(CreateView):
    """
    View for Worker List creating page.
    """
    model = WorkerList
    template_name = 'workers/worker_list_creation.html'
    form_class = WorkerListForm

    def get_success_url(self) -> str:
        return self.object.get_absolute_url()


class WorkersSearchView(WorkerListView):
    """
    Workers search on Worker List page.
    """
    def _get_workers_queryset(self) -> QuerySet:
        search_service = SearchService(self.object.workers)
        return search_service.search_by_full_name(self.request.GET['q'])

    def get_context_data(self, **kwargs) -> dict:
        kwargs['q'] = f'q={self.request.GET["q"]}&'
        return super().get_context_data(**kwargs)


worker_lists_view = WorkerListsView.as_view()
worker_list_view = WorkerListView.as_view()
worker_lists_search_view = WorkerListsSearchView.as_view()
worker_list_delete_view = DeleteView.as_view(
    model=WorkerList,
    success_url=reverse_lazy('workers:worker_lists')
)
worker_list_update_view = WorkerListUpdateView.as_view()
worker_list_create_view = WorkerListCreateView.as_view()
workers_search_view = WorkersSearchView.as_view()
