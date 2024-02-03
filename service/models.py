from django.db import models
class service(models.Model):
    service_token=models.CharField(max_length=50)
    service_link=models.URLField(max_length=100)
    
# Create your models here.
