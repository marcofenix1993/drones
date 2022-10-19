from django.db import models

ModelType = models.TextChoices('ModelType', 'Lightweight Middleweight Cruiserweight Heavyweight')
StateType = models.TextChoices('StateType', 'IDLE LOADING LOADED DELIVERING DELIVERED RETURNING')


class Medication(models.Model):
    name = models.CharField(max_length=100, default='', null=False, primary_key=True)
    code = models.CharField(max_length=100, default='', null=False)
    weight = models.IntegerField()
    image_url = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name
