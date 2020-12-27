from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    description=models.CharField(max_length=300,null=True)
    social_github=models.URLField(max_length=300,null=True)
    social_twitter=models.URLField(max_length=300,null=True)
    social_linkedin=models.URLField(max_length=300,null=True)
    social_facebook=models.URLField(max_length=300,null=True)

    image = models.ImageField(default="default.jpg",upload_to='Profile_pics')

    def __str__(self):
        return f"{self.user.username}"