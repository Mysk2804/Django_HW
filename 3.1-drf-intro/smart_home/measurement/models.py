from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f'Датчик {self.name}, Описание {self.description}'


class Measurement(models.Model):
    id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.CharField(max_length=100)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'Дата обновления {self.temperature}, температура {self.created_at}, датчик {self.id_sensor}'
