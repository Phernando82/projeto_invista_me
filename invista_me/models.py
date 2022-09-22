from django.db import models
from datetime import datetime

# documentação Django para Models: https://docs.djangoproject.com/en/3.1/topics/db/models/
class Investimento(models.Model):
    investimento = models.TextField(max_length=255)
    valor = models.FloatField()
    pago = models.BooleanField(default=False)
    data = models.DateField(default=datetime.now)


