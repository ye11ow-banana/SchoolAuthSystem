"""
Service layer for workers app.
"""
from django.db.models import QuerySet, Q

from workers.models import WorkerList, Worker


class WorkerListService:
    """
    Service class implementation of `WorkerList` model.
    """
    def __init__(self):
        self._model = WorkerList

    def search(self, data: str) -> QuerySet:
        return self._model.objects.filter(title__icontains=data)


class WorkerService:
    """
    Service class implementation of `Worker` model.
    """
    def __init__(self, model_object: WorkerList = None):
        self._object = model_object
        self._model = Worker

    def search(self, data: str) -> QuerySet:
        if self._object is None:
            return self._model.objects.none()
        return self._object.workers.filter(
            Q(first_name__icontains=data) |
            Q(middle_name__icontains=data) |
            Q(last_name__icontains=data)
        )
