from django.db import models
# from django.contrib.auth.models import User
# Create your models here.
class Position(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-id']
        verbose_name = "Позиция"
        verbose_name_plural = "Позиции"

class Level(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name

class Employers(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    middle_name = models.CharField(max_length=63)
    position = models.ManyToManyField(Position)
    user = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='children')
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.first_name + " " +  self.last_name

    class Meta:
        ordering = ['-id']
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"