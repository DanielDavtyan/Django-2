from django.db import models


class ObjectInfo(models.Model):
    cityName = models.CharField(max_length=100)

    def __str__(self):
        return self.cityName

    class Meta:
        verbose_name_plural = 'cities'





