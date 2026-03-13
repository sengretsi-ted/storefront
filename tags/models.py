from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=255) 


class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) #ContentType is a model that Django provides to keep track of all the models in the project and has been decoupled from store app
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    






    