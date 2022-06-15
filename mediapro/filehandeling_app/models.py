from django.db import models


class VenueListing(models.Model):
    name = models.CharField(max_length=60)
    address = models.TextField(max_length=100)
    contact = models.IntegerField()
    media = models.FileField(upload_to="media", null=True, blank=True, default="media/default.jpg")



# Create your models here.
