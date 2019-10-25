from django.db import models
from swampdragon.models import SelfPublishModel
from .serializers import NotificationSerializer
from django.contrib.auth.models import User


class Notification(SelfPublishModel, models.Model):
    serializer_class = NotificationSerializer
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.TextField()
