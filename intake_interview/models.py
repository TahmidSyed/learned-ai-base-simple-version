from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class client_information(models.Model):
    name = models.CharField(max_length = 200)
    date_of_birth = models.CharField(max_length = 200)
    primary_residence = models.CharField(max_length = 200)
    legal_issue = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('client_information:detail', args=[str(self.id)])
