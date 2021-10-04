from django.db import models
from django.utils import timezone

# Create your models here.

class Arduino(models.Model):
    BOARD = (
        ('EL',"Entry Level"),
        ('EF',"Enhanced Features"),
        ('IoT', "Internet of Things"),
        ('RET','Retired')
    )
    board = models.CharField(verbose_name="Board",max_length=3, choices=BOARD)
    board_name = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.board} - {self.board_name}"
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('arduinodata:arduino-data', kwargs={'pk' : self.pk})

class Data(models.Model):
    arduino = models.ForeignKey(Arduino, on_delete=models.CASCADE)
    sensor = models.IntegerField(default='0')
    content = models.TextField(verbose_name="Content",default='')
    date = models.DateField(verbose_name="Date",default='')
    def __str__(self):
        return f"Sensor {self.sensor} - {self.arduino.board_name} - {self.date}"


