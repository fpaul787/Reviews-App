from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# test
class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
