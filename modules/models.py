from django.db import models
from django.utils import timezone

# Create your models here.
class Module(models.Model):

    class Meta:

        db_table = 'module'

    name = models.CharField(max_length=100, unique=True)

class ModuleData(models.Model):

    class Meta:

        db_table = 'module_data'

    date = models.DateTimeField(default=timezone.now)
    latitude = models.DecimalField(max_digits=11, decimal_places=8, null=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, null=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    humidity = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    pressure = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    ppm = models.IntegerField(null=True)
    module = models.ForeignKey("Module", on_delete=models.CASCADE, related_name='module_data')
