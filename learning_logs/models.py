from django.db import models

# A model the app user is learning about
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def__str__(self):
    #return a string representation of the model
        return self.text
