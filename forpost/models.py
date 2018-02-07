from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Lone(models.Model):
    choice = (
        ('대출완료','대출완료'),
        ('회수중','회수중'),
        ('회수완료','회수완료'),
    )
    user_id = models.ForeignKey(User)
    attention = models.CharField(max_length=10, choices=choice, default='대출완료')
    price = models.FloatField()

    def __str__(self):
        return str(self.id)

class Payback(models.Model):
    lone_id = models.ForeignKey(Lone)
    payback = models.FloatField()
    def __str__(self):
        return str(self.id)