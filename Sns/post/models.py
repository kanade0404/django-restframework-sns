from django.db import models
from django.conf import settings


class Post(models.Model):
    post = models.CharField(max_length=140)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.post}'
