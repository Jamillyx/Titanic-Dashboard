from django.db import models


# Create your models here.
class TitanicPassenger(models.Model):
    SURVIVAL_CHOICES = [
        (0, "Não Sobreviveu"),
        (1, "Sobreviveu"),
    ]
    PCLASS_CHOICES = [
        (1, "Primeira Classe"),
        (2, "Segunda Classe"),
        (3, "Terceira Classe"),
    ]
    EMBARKED_CHOICES = [
        ("C", "Cherbourg"),
        ("Q", "Queenstown"),
        ("S", "Southampton"),
    ]
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    sex = models.CharField(max_length=10, null=True, blank=True)
    fare = models.FloatField(null=True, blank=True)
    survived = models.BooleanField(choices=SURVIVAL_CHOICES)
    embarked = models.CharField(
        max_length=1, choices=EMBARKED_CHOICES, null=True, blank=True
    )
    pclass = models.IntegerField(choices=PCLASS_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.name
