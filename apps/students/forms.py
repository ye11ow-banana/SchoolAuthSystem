from django import forms

from students.models import Subject


class SubjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.creator = kwargs.pop('creator')
        super().__init__(*args, **kwargs)

    class Meta:
        model = Subject
        fields = 'title',

    def save(self, commit=False):
        subject = super().save(commit)
        subject.add_new_creator(self.creator)
        return subject
