from django.db import models


CATEGORIES_LIST = (
    ("COMIDA", "Comida"),
    ("BEBIDA", "Bebida"),
    ("DRINKS", "Drinks"),
    ("PRATO PRINCIPAL", "Prato Principal"),
    ("SOBREMESA", "Sobremesa")
)
# Create your models here.


class Food(models.Model):
    name = models.CharField(default='title', max_length=100)
    description = models.TextField(max_length=1000)
    category = models.CharField(max_length=50, choices=CATEGORIES_LIST)
    thumb_img = models.ImageField(default='', upload_to='thumb_foods')
    
    def __str__(self):
        return self.name
