from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class Video (models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    videoFile = models.FileField(upload_to='videoFiles/')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def filename(self):
        return os.path.basename(self.videoFile.name)

# to delete de file before delete record from database
@receiver(post_delete, sender=Video)
def submission_delete(sender, instance, **kwargs):
    instance.videoFile.delete(False)
