from django.db import models


class Picture(models.Model):
    th_id = models.AutoField(primary_key=True)
    th_data = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'picture'
