from django.db import models

# Create your models here.


class SecretToken(models.Model):
    token = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.token)
