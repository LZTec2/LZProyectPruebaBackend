from django.db import models

# Create your models here.

class QR(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    content = models.TextField()
    author = models.CharField(max_length=100)
    color1 = models.CharField(max_length=7)
    color2 = models.CharField(max_length=7, null=True, blank=True)
    createdAt = models.DateTimeField()
    dotStyle = models.CharField(max_length=20)
    eyeStyle = models.CharField(max_length=20)
    isPublic = models.BooleanField(default=True)
    logoImage = models.TextField(null=True, blank=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.id})"
