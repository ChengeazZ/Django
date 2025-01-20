from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='default.jpg', blank=True)

    def __str__(self):
        return self.title