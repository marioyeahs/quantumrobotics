from django.db import models

# Create your models here.

class Arduino(models.Model):
    BOARD = (
        ('EL',"Entry Level"),
        ('EF',"Enhanced Features"),
        ('IoT', "Internet of Things"),
        ('ED','Education')
    )
    board = models.CharField(verbose_name="Board",max_length=3, choices=BOARD)
    board_name = models.CharField(max_length=255)
    def __str__(self):
        return self.board_name

class Data(models.Model):
    arduino = models.ForeignKey(Arduino, on_delete=models.CASCADE)
    data = models.TextField(verbose_name="Data")
    def __str__(self):
        return f"{self.data} - Arduino:{self.arduino}"

