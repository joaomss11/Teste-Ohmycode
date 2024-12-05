from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=50, null=True)



class Task(models.Model):
    status_options = {
        "pendente" : "pendente",
        "em andamento" : "em andamento",
        "concluído" : "concluído"
    }
    title = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(max_length=12, choices=status_options)
    user = models.ForeignKey(User, related_name='tasks', on_delete=models.SET_NULL, null=True)



    def __str__(self):
        return self.title