from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey



# Create your models here.
class LikedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #foreign key to User, with cascade delete
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) #foreign key to Product, with cascade delete
    object_id = models.PositiveIntegerField() 
    content_object = GenericForeignKey("content_type", "object_id")




