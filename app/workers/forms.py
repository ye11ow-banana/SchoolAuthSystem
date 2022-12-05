from django import forms

from workers.models import WorkerList


class WorkerListForm(forms.ModelForm):
    class Meta:
        model = WorkerList
        fields = 'title',
