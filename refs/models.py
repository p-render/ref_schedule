from django.db import models
from django.contrib.auth.models import User

class Ref(models.Model):
    user            = models.OneToOneField(User)
    first_name      = models.CharField(max_length=100)
    last_name       = models.CharField(max_length=100)

    def __unicode__(self):
        return self.user


