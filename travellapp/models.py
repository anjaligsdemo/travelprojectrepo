from django.db import models

# Create your models here.


class Features(models.Model):
    title = models.CharField(max_length=200)
    banner = models.ImageField(upload_to='home_images')
    description = models.TextField()

    def __str__(self):
        return self.title


