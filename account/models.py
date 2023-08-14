from django.db import models
from django.contrib.auth.models import User

# Create your models here.






class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    father_name = models.CharField(max_length=25)
    email = models.EmailField(null=True, blank=True)
    national_code = models.IntegerField()
    profile_image = models.ImageField(upload_to='profiles/images', blank=True , null=True)


    class Meta:
        verbose_name = "حساب کاربری"
        verbose_name_plural = "حساب های کاربری"

    def __str__(self):
        return self.user.username