"""
Service layer for workers app.
"""
from django.db.models import QuerySet, Q, Manager


class SearchService:
    """
    Service class for filtering fields in model.
    """
    def __init__(self, model_manager: Manager):
        self._model_manager = model_manager

    def search_by_full_name(self, search_input: str) -> QuerySet:
        return self._model_manager.filter(
            Q(first_name__icontains=search_input) |
            Q(middle_name__icontains=search_input) |
            Q(last_name__icontains=search_input)
        )

    def search_by_title(self, search_input: str) -> QuerySet:
        return self._model_manager.filter(title__icontains=search_input)
