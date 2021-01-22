from django.db import models

# Create your models here.
class materias(models.Model):

    id = models.AutoField(primary_key=True)
    esporte = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
class Meta:
    db_table = "materias"