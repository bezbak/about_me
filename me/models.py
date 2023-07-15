from django.db import models

# Create your models here.
class Me(models.Model):
    full_name = models.CharField(
        max_length=55
    )
    date_of_birthday = models.DateField()
    description = models.TextField()