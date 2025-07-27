from django.db import models

class Urls(models.Model):
    original_url = models.URLField(max_length=256)
    hash = models.CharField(max_length=10, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
