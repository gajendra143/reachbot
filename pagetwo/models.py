from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=20)
    mail = models.EmailField(max_length=30)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=200)


    class Meta:
        db_table = 'Register'

    def __str__(self):
        # __str__ = string representation of an object
        return self.name

class ebregister(models.Model):
    name = models.CharField(max_length=20)
    mail = models.EmailField(max_length=30)

    class Meta:
        db_table = 'ebregister'
