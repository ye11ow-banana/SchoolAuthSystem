from django.db.models import QuerySet
from django.views.generic import DetailView, ListView

from workers.models import WorkerList


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
    View for Worker List page.
    """
    model = WorkerList
    context_object_name = 'worker_list'
    template_name = 'workers/worker_list.html'


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
