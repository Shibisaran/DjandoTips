from django.db import models

# Create your models here.

class Tip(models.Model):
    CATEGORY_CHOICES = [
        ('models', 'Models'),
        ('views', 'Views'),
        ('templates', 'Templates'),
        ('forms', 'Forms'),
        ('admin', 'Admin'),
        ('security', 'Security'),
        ('deployment', 'Deployment'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    upvotes = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
