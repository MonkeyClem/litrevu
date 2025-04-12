from django.db import models
from authentication.models import User

# Create your models here.


class UserFollows(models.Model) : 
    user = models.ForeignKey(to=User, related_name="following", on_delete=models.CASCADE)
    followed_user = models.ForeignKey(to=User, on_delete=models.CASCADE,  related_name="followed_by")

    class Meta : 
        unique_together = ('user' , 'followed_user')

    def __str__(self):
        return f'{self.user} follows {self.followed_user}'
