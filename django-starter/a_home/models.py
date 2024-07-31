from django.db import models
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    resumen = models.TextField(max_length=1255)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Título: {self.title}"

