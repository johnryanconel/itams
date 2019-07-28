from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Asset(models.Model):
    name = models.CharField(max_length = 128)
    description = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('asset-detail', kwargs={'pk': self.pk})