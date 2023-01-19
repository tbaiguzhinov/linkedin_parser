from django.db import models


class Contact(models.Model):
    full_name = models.CharField(
        'Contact name',
        max_length=1000,
    )
    occupation = models.CharField(
        'Occupation',
        max_length=1000,
    )

    def __str__(self):
        return self.full_name


class Presence(models.Model):
    current_time = models.DateTimeField(
        'Time logged',
    )
    status = models.CharField(
        'Presence status',
        max_length=1000,
    )
    contact = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        related_name='presence_hours',
    )

    def __str__(self):
        return f'{self.current_time} - {self.contact}'
