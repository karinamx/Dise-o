from django.db import models

class Usuario(models.Model):
    email = models.EmailField(max_length=254)
    contraseña = models.CharField(max_length=128)
    dirección = models.CharField(max_length=255)
    dirección2 = models.CharField(max_length=255, blank=True)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    código_postal = models.CharField(max_length=20)

    def __str__(self):
        return self.email
