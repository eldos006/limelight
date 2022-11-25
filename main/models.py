from django.db import models


class Car(models.Model):
    img = models.ImageField(upload_to="images", null=True, blank=True)
    model = models.CharField(max_length=150, verbose_name='Модель')
    marka = models.CharField(max_length=150, verbose_name='Марка')
    year = models.CharField(max_length=150, verbose_name='Год')
    price = models.CharField(max_length=250, verbose_name='Цена')
    color = models.CharField(max_length=150, verbose_name='Цвет')

    def str(self):
        return self.price

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"


class News(models.Model):
    image = models.ImageField(upload_to="images", null=True, blank=True)
    title = models.CharField(max_length=150)
    data = models.DateField()
    anons = models.TextField()

    def str(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"