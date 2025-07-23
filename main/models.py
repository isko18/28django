from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название продукта"
    )
    description = models.TextField(
        verbose_name="Описание продукта"
    )
    category = models.CharField(
        max_length=255,
        verbose_name="Категория товара"
    )
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Цена"        
    )
    delivery = models.BooleanField(
        default=False,
        verbose_name="Доставка"
    )
    image = models.ImageField(
        upload_to="product/",
        verbose_name='Фото'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        