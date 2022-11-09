from django.db import models
from App_Login.models import CreateUser

# Create your models here.


class Feedback(models.Model):
    user = models.ForeignKey(CreateUser, related_name='user_feedback', on_delete=models.CASCADE)
    house_name = models.CharField(max_length=200)
    flat_number = models.CharField(max_length=200)
    feedback = models.TextField(max_length=1000)
    replay_feedback = models.TextField(max_length=1000, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.feedback

    class Meta:
        ordering = ['-created']





