from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class PerfilUsuario(AbstractUser):
    email = models.EmailField()
    edad = models.IntegerField()

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='custom_user_set',  # Nombre de relación personalizado
        related_query_name='custom_user'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_user_set',  # Nombre de relación personalizado
        related_query_name='custom_user'
    )

    def __str__(self):
        return self.username