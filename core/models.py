from pyexpat import model
from django.db import models
import uuid
# Create your models here.

class ProfileUser(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='profile')

    def __str__(self) -> str:
        return self.name

class Status(models.Model):
    user = models.ForeignKey(ProfileUser, on_delete=models.CASCADE, related_name='status')
    file = models.ImageField(upload_to='status')
