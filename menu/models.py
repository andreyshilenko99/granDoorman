from django.db import models

# Create your models here.


from django.db import models


class Event(models.Model):
    camera_id = models.CharField(max_length=20)
    time = models.DateTimeField(auto_now=False, auto_now_add=False)
    link = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.time


# class FilterEvent(models.Model):
#     camera_id = models.ManyToManyField(Event.camera_id)
#     time = models.ManyToManyField(Event.time)
#     link = models.ManyToManyField(Event.link)
