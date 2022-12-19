from django.conf.global_settings import AUTH_USER_MODEL
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Subject(models.Model):
    """
    Subject that students study at school.
    """
    title = models.CharField('Title', max_length=255)
    creator = models.ForeignKey(
        AUTH_USER_MODEL, verbose_name='creator',
        on_delete=models.DO_NOTHING
    )
    owners = models.ManyToManyField(
        AUTH_USER_MODEL, verbose_name='owners',
        related_name='subjects'
    )

    class Meta:
        db_table = 'subject'
        verbose_name = 'subject'
        verbose_name_plural = 'subjects'

    def __str__(self) -> str:
        return str(self.title)

    def get_absolute_url(self) -> str:
        return reverse(
            'students:subject_detail', args=[self.pk],
            current_app='students'
        )

    def add_new_creator(self, creator: User) -> None:
        self.creator = creator
        self.save()
