from django.db import models

# Create your models here.

class Shares(models.Model):
    code = models.CharField('Code', max_length=10)
    name = models.CharField('Name', max_length=50)
    open = models.DecimalField('Open', max_digits=7, decimal_places=2)
    high = models.DecimalField('High', max_digits=7, decimal_places=2)
    low = models.DecimalField('Low', max_digits=7, decimal_places=2)
    close = models.DecimalField('Close', max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name
