from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    value = models.IntegerField()
    description = models.TextField()

    class Meta:
        db_table = 'item'
        indexes = [
            models.Index(fields=['name'], name='item_name_idx'),
            models.Index(fields=['value'], name='item_value_idx'),
        ]