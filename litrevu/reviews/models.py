from django.db import models
from tickets.models import Ticket
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
User = get_user_model()

# Create your models here.



class Review(models.Model) : 
    ticket = models.ForeignKey(to= Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5) ])
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.headline} ({self.rating}/5) par {self.user}"