from django.db import models

class Contato(models.Model):
    nome_completo = models.CharField(max_length=250)
    relação = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    numero = models.CharField(max_length=15)
    endereco = models.CharField(max_length=200)


    def __str__(self) :
        return self.nome_completo