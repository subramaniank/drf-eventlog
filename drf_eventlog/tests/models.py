from django.db import models

class TestAutoIncrementModel(models.Model):
    """
    Model for testing with autoincrementing primary keys
    """

    name = models.CharField(max_length=50)
    rank = models.IntegerField()
    clash = models.BooleanField(default=False)
    
