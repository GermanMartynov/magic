from django.db import models

# Create your models here.


class Feature(models.Model):
    """ Таблица свойств """
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    # class Meta:
    #     db_table = 'Свойства'


class Value(models.Model):
    """Таблица значений"""
    has = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.has


class FeatureValue(models.Model):
    """Таблица пар значений Свойство: значение"""
    feature = models.ForeignKey(Feature)
    value = models.ForeignKey(Value)

    class Meta:
        """уникальное значение двух колонок"""
        unique_together = [
            ('feature', 'value'),
        ]

    def __str__(self):
        return str(self.feature) + ': ' + str(self.value)
