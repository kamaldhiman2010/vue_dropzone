import imp
from re import I
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class FileData(models.Model):
    uuid = models.CharField(max_length=200,blank=True,null=True)
    file_name = models.CharField(max_length=100,blank=True,null=True)
    images = models.ImageField(
        _("Image"), upload_to=upload_to)
    
    def __str__(self):
        return self.file_name
    
