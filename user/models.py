from django.db import models

class User(models.Model):
    first_name = models.CharField(verbose_name="First Name", max_length=30)
    last_name = models.CharField(verbose_name="Last Name", max_length=30)
    username = models.CharField(verbose_name="Username", max_length=30, unique=True)
    password = models.CharField(verbose_name="Password", max_length=20)
    email = models.EmailField(verbose_name="Email", max_length=30)

    def __str__(self):
        return self.name
