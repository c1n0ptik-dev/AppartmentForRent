from django.db import models

class Apartment(models.Model):

    address = models.CharField(max_length=100, unique=True, null=False) # адреса квартири
    complex = models.CharField(max_length=50, null=False)  # ЖК
    price = models.CharField(max_length=50, null=False)  # Ціна
    area = models.CharField(max_length=50, null=False)  # Площа
    room = models.CharField(max_length=50, null=False)  # Кімната
    floor = models.CharField(max_length=50, null=False)  # Поверх
    content = models.TextField(max_length=1024, null=False)
    image1 = models.FileField(null=False, upload_to='upload/')
    image2 = models.FileField(null=False, upload_to='upload/')
    image3 = models.FileField(null=False, upload_to='upload/')
    image4 = models.FileField(null=False, upload_to='upload/')

    def __str__(self) -> str:
        return str(self.address)




