from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=30)
    author_name = models.CharField(max_length=30)
    author_last_name = models.CharField(max_length=30)
    year = models.PositiveIntegerField(blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='book_image/', default='default.png', blank=True, null=True)

    class Meta:
        verbose_name = 'books'

    def __str__(self):
        return f"{self.title} ({self.author_name} {self.author_last_name})"





