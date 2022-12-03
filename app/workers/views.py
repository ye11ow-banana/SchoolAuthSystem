from django.views.generic import DetailView, ListView

from workers.models import WorkerList


class WorkerListsView(ListView):
    model = WorkerList
    paginate_by = 4
    context_object_name = 'worker_lists'
    template_name = 'workers/worker_lists.html'


class WorkerListView(DetailView):
    model = WorkerList
    context_object_name = 'worker_list'
    template_name = 'workers/worker_list.html'


worker_lists_view = WorkerListsView.as_view()
worker_list_view = WorkerListView.as_view()
