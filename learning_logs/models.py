from django.db import models
from django.contrib.auth.models import User

# A model the app user is learning about
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
    #return a string representation of the model
        return self.text

#Entry class provides something specific about a topic
class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Entries'

    def __str__(self):
    #return a string representation of the Model
        return self.text[:50] + "..."
