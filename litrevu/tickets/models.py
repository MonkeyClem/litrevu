from django.db import models
from authentication.models import User

# Create your models here.

class Ticket(models.Model): 
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=2048, blank = True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ticket_images/', null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
 

    def __str__(self):
        return f"{self.title} par {self.user}, at {self.time_created} "