from django.db import models

# Create your models here.
class Name(model.Model):
	n_id = models.IntegerField(max_length=32)

