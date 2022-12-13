from django.db import models


class Subject(models.Model):
    """
    Subject that students study at school.
    """
    title = models.CharField('Title', max_length=255)

    class Meta:
        db_table = 'subject'
        verbose_name = 'subject'
        verbose_name_plural = 'subjects'

    def __str__(self) -> str:
        return str(self.title)
